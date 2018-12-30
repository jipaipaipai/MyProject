# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 20:42:09 2018

@author: haoyu
"""

import numpy as np
import pandas as pd
import os
import jieba
from keras.models import load_model
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

path = r'D:\软件\微信\文件\WeChat Files\liuhaoyun123456\Files\项目\北京教科院\社会实践\1219\\'
filenames = os.listdir(path+'model\\')
data_all = pd.read_pickle(path+'数据\\all.pickle')
data_all.index = [i for i in range(len(data_all))]#序列重排
out = data_all.iloc[:,[1,3,5,6,8,-4]]
texts_word = out['感受'].tolist()
texts_word = [str(i) for i in texts_word]
texts = [jieba.lcut(str(i)) for i in texts_word]

# =============================================================================
# #句子长度
# word_len = [len(i) for i in texts]
# word_count = pd.Series(word_len).value_counts()
# df_word_len = pd.DataFrame(word_count)
# df_word_len.to_excel(path+'数据\\'+'word_len.xlsx')
# =============================================================================

maxlen = 50  # We will cut reviews after 100 words
max_words = 10000  # We will only consider the top 10,000 words in the dataset
tokenizer = Tokenizer(num_words=max_words)
tokenizer.fit_on_texts(texts)
sequences = tokenizer.texts_to_sequences(texts)
word_index = tokenizer.word_index
print('Found %s unique tokens.' % len(word_index))

data = pad_sequences(sequences, maxlen=maxlen)
print('Shape of data tensor:', data.shape)

count = 1
for filename in filenames:
    model = load_model(path+'model\\'+filename)
    temp = model.predict_classes(data)
    temp1 = pd.DataFrame(temp)
    temp1.columns = [filename[:-3]]
    out = pd.concat([out,temp1],axis=1)
    print('loop:',count)
    count += 1

out.to_pickle(path+'数据\\'+'encoding2.pickle')
out.to_excel(path+'数据\\'+'encoding2.xlsx')

































