# 基于注意力机制的RNN翻译器
## 介绍
本程序实现了一个基于注意力机制的RNN翻译器，并通过在平行双语语料库(bilingual parallel corpora)上训练一定次数后，达到翻译某种语言的能力。\
本程序另外附加了两个python脚本，分别用来将xml语料库文件转换为txt，以及从语料库构建新的词汇表。
## 运行环境
本程序在python3.6下运行，需要软件包“tensorflow=2.0.0”以及“nltk=3.4.5”；若使用GPU版本的该软件包（即tensorflow-gpu=2.0.0），则还需要支持CUDA的NVIDIA GPU、CUDA toolkit 10.0，以及cuDNN 7.6.0。
## 方法
神经网络的基本单元采用“附门循环单元”(gated recurrent unit, GRU)，该结构在2014年由赵镜贤(Kyunghyun Cho)提出。\
注意力机制采用Dzmitry Bahdanau于2015年提出的注意力模型。\
具体程序使用Google的tensorflow软件包构建；训练过程中的求参数梯度与参数优化均使用tensorflow提供的工具。
## 系统框架
本程序的组成部分包括参数解析器(argument parser，文件名为myparser.py)、文本数据处理器（dataset creator，文件名为mytxtreader.py）、模型（model，文件名为model.py），以及训练器（trainer，文件名为main.py）。训练器同时完成主程序的工作。\
在程序结构中，训练器调用其它全部模块；其它模块之间没有相互调用关系。
## 实现细节
### 参数解析器
调用了python库中的argparse模块，用于读入参数。
### 文本数据处理器
使用tensorflow（下称tf）的data.TextLineDataset方法从文本文档建立字符串组成的数据集。\
用tf.strings.split方法将字符串分割成词汇。\
用模块tf.python.ops.lookup_ops下的方法构建了对应单词的哈希表并将词汇向量映射到离散数字向量。\
### 模型
使用tf.keras.layers模块（下称layers）进行了快捷的构建：\
RNN的主体部分采用layers.GRU方法构建。\
嵌入层以及映射层分别采用layers.Embedding与layers.Dense方法构建。\
Bahadnau Attention的部分包含三个全连接网络，均使用layers.Dense方法构建。\
损失函数采用tf.keras.losses.SparseCategoricalCrossentropy方法。
### 训练器
使用tf.GradientTape方法进行梯度计算；使用tf.keras.optimizers.Adam进行优化。
## 使用说明
### 程序主体
运行python3 main.py --help 以获得关于参数的描述。
默认训练超参如下：嵌入维数64，RNN隐藏层维数128，单批句数64，学习率0.001，训练次数2000轮，每100轮输出信息。
按照您想要的参数运行python3 main.py。
### 小工具
运行python3 corpus_to_vocab.py，并按程序指示输入您的输入输出路径。
运行python3 xml_to_txt.py，并按程序指示输入您的输入输出路径。
