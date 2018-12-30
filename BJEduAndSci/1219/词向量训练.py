# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 20:39:26 2018

@author: haoyu
"""

from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import numpy as np
import pandas as pd
import os
import jieba

###数据处理
path = r'D:\软件\微信\文件\WeChat Files\liuhaoyun123456\Files\项目\北京教科院\社会实践\1219\\'
filenames = os.listdir(path+'数据\\')
data_word = pd.read_excel(path+'数据\\'+filenames[8])
data_word = data_word.dropna()
texts_word = data_word.ix[:,'感受'].tolist()
texts = [jieba.lcut(str(i)) for i in texts_word]
word_len = [len(i) for i in texts]

#词向量维度设置
maxlen = 60  # We will cut reviews after 100 words
training_samples = int(0.5*len(texts))  # We will be training on 200 samples
validation_samples = int(0.3*len(texts))  # We will be validating on 10000 samples
max_words = 10000  # We will only consider the top 10,000 words in the dataset

tokenizer = Tokenizer(num_words=max_words)
tokenizer.fit_on_texts(texts)
sequences = tokenizer.texts_to_sequences(texts)

word_index = tokenizer.word_index
print('Found %s unique tokens.' % len(word_index))

data = pad_sequences(sequences, maxlen=maxlen)
labels = data_word.iloc[:,6:]
labels = np.asarray(labels.values.tolist())
print('Shape of data tensor:', data.shape)
print('Shape of label tensor:', labels.shape)

#打乱训练数据
# Split the data into a training set and a validation set
# But first, shuffle the data, since we started from data
# where sample are ordered (all negative first, then all positive).
indices = np.arange(data.shape[0])
np.random.shuffle(indices)
data = data[indices]
labels = labels[indices]
x_train = data[:training_samples]
y_train = labels[:training_samples,0]
x_val = data[training_samples: training_samples + validation_samples]
y_val = labels[training_samples: training_samples + validation_samples,0]
x_test = data[training_samples + validation_samples:]
y_test = labels[training_samples + validation_samples:,0]


embedding_dim = 100
from keras.models import Sequential
from keras.layers import Embedding, Flatten, Dense, Conv1D, MaxPooling1D, GlobalMaxPooling1D

model = Sequential()
model.add(Embedding(max_words, embedding_dim, input_length=maxlen))

model.add(Conv1D(32,6,activation='relu'))
model.add(MaxPooling1D(5))
model.add(Conv1D(32,6,activation='relu'))
model.add(GlobalMaxPooling1D())
#model.add(MaxPooling1D(5))
#model.add(Flatten())

# =============================================================================
# model.add(Flatten())
# model.add(Dense(128, activation='relu'))
# model.add(Dense(64, activation='relu'))
# model.add(Dense(32, activation='relu'))
# =============================================================================

model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.summary()
model.compile(optimizer='rmsprop',
              loss='binary_crossentropy',
              metrics=['acc'])
history = model.fit(x_train, y_train,
                    epochs=8,
                    batch_size=64,
                    validation_data=(x_val, y_val))

model.evaluate(x_test,y_test)
predict = model.predict(x_test)
predict2 = model.predict_classes(x_test)
sum(predict2)
sum(y_test)
a = model.predict_classes(x_train)
sum(a)
sum(y_train)

model.save(path+'model\\'+'wtjj_2.h5')


import matplotlib.pyplot as plt

acc = history.history['acc']
val_acc = history.history['val_acc']
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = range(1, len(acc) + 1)

plt.plot(epochs, acc, 'bo', label='Training acc')
plt.plot(epochs, val_acc, 'b', label='Validation acc')
plt.title('Training and validation accuracy')
plt.legend()

plt.figure()

plt.plot(epochs, loss, 'bo', label='Training loss')
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.legend()
plt.show()





# =============================================================================
# '''调整数据比例'''
# #训练数据
# temp = pd.read_excel(path+'数据\\'+filenames[8])
# temp1_word = temp[temp['价值体认']==1]
# temp2_word = temp[temp['价值体认']==0]
# data_word = pd.concat([temp1_word[:2*len(temp2_word)],temp2_word])
# data_word = data_word.dropna()
# texts_word = data_word.ix[:,'感受'].tolist()
# texts = [jieba.lcut(str(i)) for i in texts_word]
# word_len = [len(i) for i in texts]
# 
# #预测数据
# temp = temp.dropna()
# temp_word = temp.ix[:,'感受'].tolist()
# temp_texts = [jieba.lcut(str(i)) for i in temp_word]
# 
# maxlen = 60  # We will cut reviews after 100 words
# max_words = 10000  # We will only consider the top 10,000 words in the dataset
# 
# temp_tokenizer = Tokenizer(num_words=max_words)
# temp_tokenizer.fit_on_texts(temp_texts)
# temp_sequences = temp_tokenizer.texts_to_sequences(temp_texts)
# 
# temp_data = pad_sequences(temp_sequences, maxlen=maxlen)
# temp_labels = temp.iloc[:,6:]
# temp_labels = np.asarray(labels[:,0].tolist())
# print('Shape of data tensor:', data.shape)
# print('Shape of label tensor:', labels.shape)
# 
# model.evaluate(temp_data,temp_labels)
# predict = model.predict(temp_data)
# predict2 = model.predict_classes(temp_data)
# sum(predict2)
# sum(temp_labels)
# =============================================================================











