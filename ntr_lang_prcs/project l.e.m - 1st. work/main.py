#Copyright 2019 Lab Mikazu. All Rights Reserved.
#Project "Words and Melodies" 1st. work
from __future__ import absolute_import, division, print_function, unicode_literals

import argparse
import tensorflow as tf
import numpy as np
import os
import time
from tensorflow.python.ops import lookup_ops
import nltk

import myparser
import mytxtreader
import model

UNK = "<unk>"
SOS = "<s>"
EOS = "</s>"
UNK_ID = 1
SOS_ID = 2
EOS_ID = 3


def main():
#define parser
    parser = argparse.ArgumentParser()
    myparser.myaddarguments(parser)

#parse and create hyperparameters
    MYARGS = parser.parse_args()
    hparams = myparser.mycreateparams(MYARGS)

#read dataset
    start = time.time()
    mydataset = mytxtreader.mydatasetcreator(hparams)
    print("Data set constructed within {} sec.\n".format(time.time() - start))

#test output
#    for (x, y) in mydataset:
#        print(x, y)

#define model and checkpoint
    encoder = model.Encoder(hparams)
    decoder = model.Decoder(hparams)
    optimizer = tf.keras.optimizers.Adam(learning_rate=hparams.rate)

    checkpoint_dir = './training_checkpoints'
    checkpoint_prefix = os.path.join(checkpoint_dir, "ckpt")
    checkpoint = tf.train.Checkpoint(optimizer=optimizer,
                                     encoder=encoder,
                                     decoder=decoder)
    output_file = open("output.txt", "a")

#define training process
    @tf.function
    def train_step(inp, targ, enc_hidden):
        loss = 0
        with tf.GradientTape() as tape:
            enc_output, enc_hidden = encoder(inp, enc_hidden)
            dec_hidden = enc_hidden
            dec_input = tf.fill([hparams.batch, 1], SOS_ID)
            for t in range(targ.shape[1]):
                predictions, dec_hidden, _ = decoder(dec_input, dec_hidden, enc_output)
                loss += model.loss_function(
                    tf.reshape(tf.slice(targ, [0, t], [-1, 1]), [-1]),
                    predictions)
                dec_input = tf.slice(targ, [0, t], [-1, 1])
        batch_loss = (loss / int(targ.shape[1]))
        variables = encoder.trainable_variables + decoder.trainable_variables
        gradients = tape.gradient(loss, variables)
        optimizer.apply_gradients(zip(gradients, variables))
        return batch_loss

#define translate process
    srcvocabpath = "%s.%s" % (hparams.vocab_prefix, hparams.src)
    sv = lookup_ops.index_table_from_file(srcvocabpath, default_value=UNK_ID)
    tgtvocabpath = "%s.%s" % (hparams.vocab_prefix, hparams.tgt)
    tv = lookup_ops.index_table_from_file(tgtvocabpath, default_value=UNK_ID)
    temptv = tf.data.TextLineDataset(tgtvocabpath)
    i = 0
    for x in temptv:
        i += 1
    temptv = temptv.batch(i)
    for x in temptv:
        tv_reverse = x
    def scan_tv(predicted_id, tv_reverse, size):
        return tv_reverse[predicted_id]
    def translate(inputs, hparams):
        result = ''
        hidden = [tf.zeros((1, hparams.num_units))]
        enc_out, enc_hidden = encoder(inputs, hidden)
        dec_hidden = enc_hidden
        dec_input = tf.fill([1, 1], SOS_ID)
        for t in range(hparams.max_input_length):
            predictions, dec_hidden, attention_weights = decoder(
                dec_input,
                dec_hidden,
                enc_out)
            predicted_id = tf.argmax(predictions[0]).numpy()
            word = scan_tv(predicted_id, tv_reverse, hparams.tgt_vocab_size)
            result += word + ' '
            if predicted_id == EOS_ID:
                return result
        return result

#train
    if hparams.mode == "train_start" or hparams.mode == "train_continue":
        if hparams.mode != "train_start":
            start = time.time()
            checkpoint.restore(tf.train.latest_checkpoint(checkpoint_dir))
            print("Checkpoint loaded within {} sec.\n".format(time.time() - start))
        EPOCHS = hparams.num_train_steps
        start = time.time()
        for epoch in range(EPOCHS):
            enc_hidden = encoder.initialize_hidden_state()
            total_loss = 0
            for (inp, targ) in mydataset:
                batch_loss = train_step(inp, targ, enc_hidden)
                total_loss += batch_loss
            if (epoch + 1) % (hparams.steps_per_stats) == 0:
                print('Epoch {} Loss {:.4f}'.format(epoch + 1,
                    total_loss / hparams.train_data_size))
                print('Time taken for {} epoch {} sec\n'.format(hparams.steps_per_stats,
                    time.time() - start))
                output_file.write('Epoch {} Loss {:.4f}'.format(epoch + 1,
                    total_loss / hparams.train_data_size))
                output_file.write('Time taken for {} epoch {} sec\n'.format(hparams.steps_per_stats,
                    time.time() - start))
                start = time.time()
            if (epoch + 1) % (hparams.steps_per_stats * 10) == 0:
                checkpoint.save(file_prefix = checkpoint_prefix)
                print("Checkpoint saved.\n")
                output_file.write("Checkpoint saved.\n")

#translate
    if hparams.mode == "translate":
        start = time.time()
        checkpoint.restore(tf.train.latest_checkpoint(checkpoint_dir))
        print("Checkpoint loaded within {} sec.\n".format(time.time() - start))
        while True:
            input_sentence = input("Input your sentence here:\n")
            inp = tf.strings.split([input_sentence]).values
            inp = tf.dtypes.cast(sv.lookup(inp), tf.int32)
            inp = tf.reshape(inp, [1, -1])
            result = translate(inp, hparams)
            print(result)

#create test set
    srctstpath = "%s.%s" % (hparams.test_prefix, hparams.src)
    tgttstpath = "%s.%s" % (hparams.test_prefix, hparams.tgt)
    srctstdata = tf.data.TextLineDataset(srctstpath)
    tgttstdata = tf.data.TextLineDataset(tgttstpath)
    tstdata = tf.data.TextLineDataset.zip((srctstdata, tgttstdata))

#define score function
    def scorefunction(x, y, evalparams):
        x = x.numpy()
        y = y.numpy()
        candidate = x.split()
        reference = y.split()
        return nltk.translate.bleu_score.sentence_bleu([reference], candidate, evalparams)

#test
    if hparams.mode == "evaluate":
        start = time.time()
        checkpoint.restore(tf.train.latest_checkpoint(checkpoint_dir))
        print("Checkpoint loaded within {} sec.\n".format(time.time() - start))
        evalparams = input("Enter the weights for unigrams, bigrams, trigrams and so on, separating with space: ")
        evalparams = evalparams.split()
        i = 0
        for x in evalparams:
            evalparams[i] = float(x)
            i += 1
        sumscore = 0
        i = 0
        for x, y in tstdata:
            x = tf.strings.split([x]).values
            x = tf.dtypes.cast(sv.lookup(x), tf.int32)
            x = tf.reshape(x, [1, -1])
            transx = translate(x, hparams)
            score = scorefunction(transx, y, evalparams)
            sumscore += score
            i += 1
            print("Score {} on {}-th test sentence.".format(score, i+1))
        print("Overall score: {}".format(sumscore / i))


if __name__ == "__main__":
    main()
