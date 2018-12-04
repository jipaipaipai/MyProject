# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 08:17:13 2018

@author: haoyu
"""

'''词云，情感，地点和情感结合'''


import numpy as np
import pandas as pd
import jieba
import jieba.analyse
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

path = 'D:\\软件\\微信\\文件\\WeChat Files\\liuhaoyun123456\\Files\\项目\\北京教科院\\社会实践\\0921\\'
#data = pd.read_excel(path +'数据\\' +'房山区2017-2018学年数据20180920.xlsx')
#data = pd.read_excel(path +'数据\\' +'东城区2017-2018学年数据20180920.xlsx')#读取excel
#pd.to_pickle(data, path+'dc')
data = pd.read_pickle(path+'fs')
name_act = data.活动名称.tolist()
name_sch = data.学校名称.tolist()
name_gro = data.活动类型.tolist()
name_cat = data.考核类型.tolist()

name_act = list(set(name_act))#去除重复项
#name_act.remove(0.0)
name_act_list = ''.join(name_act)

#按照活动类型进行分割
name_gro = list(set(name_gro))#提取活动类型分类
word_gro = []
for i in range(len(name_gro)):#将相同分类的活动名称整合
    word_gro.append(list(set(data.loc[data.活动类型 == name_gro[i], '活动名称'].tolist())))
for i in range(len(word_gro)):#去除数值型
    if 0 in word_gro[i]:
        word_gro[i].remove(0.0)
    else:
        continue
word_gro[0][25]='x'

#按照学校进行分割
name_sch = list(set(name_sch))
word_sch = []
for i in range(len(name_sch)):
    word_sch.append(list(set(data.loc[data.学校名称 == name_sch[i], '活动名称'].tolist())))
for i in range(len(word_sch)):#去除数值型
    if 0 in word_sch[i]:
        word_sch[i].remove(0.0)
    else:
        continue

#for i in range(36):
 #   word_sch[i][33] = 's'  


#按照考核类型进行分割
name_cat = list(set(name_cat))
word_cat = []
for i in range(len(name_cat)):
    word_cat.append(list(set(data.loc[data.考核类型 == name_cat[i], '活动名称'].tolist())))
for i in range(len(word_cat)):#去除数值型
    if 0 in word_cat[i]:
        word_cat[i].remove(0.0)
    else:
        continue
for i in range(32):
    word_cat[i][27] = 's'  

'''进行分词'''
#对活动类型分类进行分词
word_gro_join = [''.join(word_gro[i]) for i in range(len(word_gro))]
wordseg_gro = []
for i in range(len(word_gro)):
    wordseg_gro.append(list(set(jieba.lcut(word_gro_join[i]))))

#对学校分类进行分词
word_sch_join = [''.join(word_sch[i]) for i in range(len(word_sch))]
wordseg_sch = []
for i in range(len(word_sch)):
    wordseg_sch.append(list(set(jieba.lcut(word_sch_join[i]))))

#对考核类型分类进行分词
word_cat_join = [''.join(word_cat[i]) for i in range(len(word_cat))]
wordseg_cat = []
for i in range(len(word_cat)):
    wordseg_cat.append(list(set(jieba.lcut(word_cat_join[i]))))


'''
#FoolNLTK分词试用
aaa = fool.analysis(word_gro_join)
result_class = []
result_word = []
for i in range(len(aaa[1][1])):
    result_class.append(aaa[1][1][i][2])
    result_word.append(aaa[1][1][i][3])
result_class_set = list(set(result_class))
org = []
'''



'''制作词云'''
#对活动类型分类进行词云制作
backgroud_Image = plt.imread(path + '词云\\词云5.jpg')
wc = WordCloud(font_path='simhei.ttf',background_color='white', max_words=500, mask=backgroud_Image)
for i in range(len(name_gro)):
    wc.generate(' '.join(wordseg_gro[i]))
    plt.imshow(wc)
    plt.axis("off")
    plt.savefig(path+'活动分类词云\\'+name_gro[i]+'.png', dpi=1000)
    plt.show()



'''
def stopwordslist(filepath):  
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]  
    return stopwords

def seg_sentence(sentence):  
    sentence_seged = jieba.cut(sentence.strip())  
    stopwords = stopwordslist(path + 'stopword.txt')  # 这里加载停用词的路径  
    outstr = []  
    for word in sentence_seged:  
        if word not in stopwords:  
            if (word != '\t') & (word != ' '):  
                outstr.append(word)
    return outstr 
word_act = seg_sentence(name_act_list)
#提取关键词
keywords = jieba.analyse.extract_tags(name_act_list, topK=100, withWeight=True)
keywords2 = jieba.analyse.textrank(name_act_list, topK=100, withWeight=True)

#制作词云

keyword_dic = dict()
for i in keywords2:
    keyword_dic[i[0]]=i[1]
backgroud_Image = plt.imread(path + 'wordcloud2.jpg')
graph = np.array(backgroud_Image)
wc = WordCloud(font_path='simhei.ttf',background_color='Black', max_words=100, mask=backgroud_Image)
wc.generate_from_frequencies(keyword_dic)
image_color = ImageColorGenerator(graph)
plt.imshow(wc)
plt.imshow(wc.recolor(color_func=image_color))
plt.axis("off")
plt.show()
'''


'''
#活动区县统计
act_loc = data['活动区县'].value_counts()

import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['font.family']='sans-serif'
mpl.rcParams['font.size'] = 6


x=np.arange(len(act_loc))+1 #设置y轴的数值，需将numbers列的数据先转化为数列，再转化为矩阵格式
y=np.array(list(act_loc))
xticks1=list(act_loc.index) #构造不同课程类目的数列
plt.bar(x,y,width = 0.35,align='center',color = 'c',alpha=0.8)#画出柱状图
#设置x轴的刻度，将构建的xticks代入，同时由于课程类目文字较多，在一块会比较拥挤和重叠，因此设置字体和对齐方式
plt.xticks(x,xticks1,size='small',rotation=30)
plt.title('活动区县分布')
for a,b in zip(range(18), act_loc):
    plt.text(a+1, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=6)
plt.savefig(path+'fs活动区县分布'+'.png',dpi=1000)
plt.show()
'''


'''
#活动地点统计
act_area = data['活动地点'].value_counts()
act_area = act_area[:25]

import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['font.family']='sans-serif'
mpl.rcParams['font.size'] = 5


x=np.arange(len(act_area))+1 #设置y轴的数值，需将numbers列的数据先转化为数列，再转化为矩阵格式
y=np.array(list(act_area))
xticks1=list(act_area.index) #构造不同课程类目的数列
plt.bar(x,y,width = 0.35,align='center',color = 'c',alpha=0.8)#画出柱状图
#设置x轴的刻度，将构建的xticks代入，同时由于课程类目文字较多，在一块会比较拥挤和重叠，因此设置字体和对齐方式
plt.xticks(x,xticks1,size='small',rotation=60)
plt.title('活动地点分布')
for a,b in zip(range(len(act_area)), act_area):
    plt.text(a+1, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=5)
plt.savefig(path+'fs活动地点分布'+'.png',dpi=1000)
plt.show()
'''














