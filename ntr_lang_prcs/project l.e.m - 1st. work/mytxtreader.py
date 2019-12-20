import tensorflow as tf
from tensorflow.python.ops import lookup_ops

UNK = "<unk>"
SOS = "<s>"
EOS = "</s>"
UNK_ID = 1
SOS_ID = 2
EOS_ID = 3


def mydatasetcreator(hparams):

    srcvocabpath = "%s.%s" % (hparams.vocab_prefix, hparams.src)
    sv = lookup_ops.index_table_from_file(srcvocabpath, default_value=UNK_ID)
    tgtvocabpath = "%s.%s" % (hparams.vocab_prefix, hparams.tgt)
    tv = lookup_ops.index_table_from_file(tgtvocabpath, default_value=UNK_ID)
    hparams.src_vocab_size = sv.size()
    hparams.tgt_vocab_size = tv.size()

    srcpath = "%s.%s" % (hparams.train_prefix, hparams.src)
    tgtpath = "%s.%s" % (hparams.train_prefix, hparams.tgt)
    srcdata = tf.data.TextLineDataset(srcpath)
    srcdata = srcdata.map(lambda x: tf.strings.split([x]).values)
    srcdata = srcdata.map(lambda x: tf.dtypes.cast(sv.lookup(x), tf.int32))
    max_length = max(tf.shape(v)[0] for v in srcdata)
    hparams.max_input_length = max_length
    srcdata = srcdata.padded_batch(hparams.batch, [max_length], drop_remainder=True)
    tgtdata = tf.data.TextLineDataset(tgtpath)
    tgtdata = tgtdata.map(lambda x: tf.strings.split([x]).values)
    tgtdata = tgtdata.map(lambda x: tf.concat([x, [EOS]], -1))
    tgtdata = tgtdata.map(lambda x: tf.dtypes.cast(tv.lookup(x), tf.int32))
    max_length = max(tf.shape(v)[0] for v in tgtdata)
    hparams.max_output_length = max_length
    tgtdata = tgtdata.padded_batch(hparams.batch, [max_length], drop_remainder=True)
    d = tf.data.TextLineDataset.zip((srcdata, tgtdata))


    for x in d:
        hparams.train_data_size += 1

    return d