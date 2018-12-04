# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 16:10:26 2018

@author: haoyun
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

path = 'D:\\软件\\微信\\文件\\WeChat Files\\liuhaoyun123456\\Files\\项目\\北京教科院\\社会实践\\1030\\'
data = pd.read_excel(path+'东城区活动地点频数表.xlsx')
#data = pd.read_excel(path+'房山区活动地点频数表.xlsx')

backgroud_Image = plt.imread(path + '词云\\词云2.jpg')
wc = WordCloud(font_path='simhei.ttf',background_color='white', max_words=500, mask=backgroud_Image)

dict_word_zx = dict(zip(data['loc'].values[:],data['f'].values[:]))
wc.generate_from_frequencies(dict_word_zx)
plt.imshow(wc)
plt.axis("off")
plt.savefig(path+'词云\\dc地点.png', dpi=1000)
#plt.savefig(path+'词云\\fs地点.png', dpi=1000)
plt.show()







