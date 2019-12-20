import tensorflow as tf

corpuspath = input("Input the path for your corpus: ")
vocabpath = input("Input the path for the output vocabulary: ")
dataset = tf.data.TextLineDataset(corpuspath)

vocabulary_set = set()
for text_tensor in dataset:
  some_tokens = tf.strings.split([text_tensor]).values
  vocabulary_set.update(some_tokens.numpy())

s = tf.convert_to_tensor(list(vocabulary_set))
s = tf.strings.join(s, separator='\n')
s = tf.strings.join(["<emp>\n<unk>\n<s>\n</s>\n", s])
tf.io.write_file(vocabpath, s)

print("Succeeded.")
