# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 22:30:43 2018

@author: haoyun
"""

import pandas as pd
import numpy as np
import jieba
import os
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
path = 'D:\\软件\\微信\\文件\\WeChat Files\\liuhaoyun123456\\Files\\项目\\北京教科院\\社会实践\\1030\\'
filenames = os.listdir(path+'数据\\')

# =============================================================================
# '''第一部分：提取情感词'''
# #读取所需文件
# 
# dc = pd.read_excel(path+'数据\\'+filenames[0])
# #dc = pd.read_excel(path+'数据\\'+filenames[1])
# qgc = pd.read_excel(path+'情感词汇本体\\'+'情感词汇本体.xlsx')
# 
# #提取感受部分并进行分词
# temp_gs = dc['感受'].values.tolist()
# cut_gs = [jieba.lcut(i) for i in temp_gs if type(i) == str ]
# 
# #将情感词表中读入词语一列，以便之后进行筛选
# temp_cy = qgc['词语'].values.tolist()
# 
# #将分词结果遍历情感词表，筛选出情感词并且提取出强度和极性
# cut_qgc = []
# qd = []
# jx = []
# for m in cut_gs:
#     temp_qgc = m
#     temp_cut_qgc = []
#     temp_qd = []
#     temp_jx = []
#     for n in temp_qgc:
#         if n in temp_cy:
#             index = temp_cy.index(n)
#             temp_cut_qgc.append(n)
#             temp_qd.append(qgc['强度'][index])
#             temp_jx.append(qgc['极性'][index])
#         else:
#             continue
#     cut_qgc.append(temp_cut_qgc)
#     qd.append(temp_qd)
#     jx.append(temp_jx)
# 
# #将得到的结果输出为xlsx和pickle文件作为中间文件，以便下次读取，无需再运行
# result = [cut_qgc, qd, jx]
# df_result = pd.DataFrame(np.array(result).T)
# df_result.to_pickle(path+'dc_qgc')
# df_result.to_excel(path+'dc_qgc.xlsx')
# #df_result.to_pickle(path+'fs_qgc')
# #df_result.to_excel(path+'fs_qgc.xlsx')
# =============================================================================


# =============================================================================
# '''第二部分：情感词分类并计算得分'''
# #读取并清洗分类完的数据
# df_result1 = pd.read_pickle(path+'dc_qgc')
# #df_result1 = pd.read_pickle(path+'fs_qgc')
# list_result1 = df_result1.values.tolist()
# list_result1 = [i for i in list_result1 if len(i[0]) != 0]
# #temp = list_result1[:10]
# 
# #将词性进行分类，并且计算得分
# zx = []
# bao = []
# bian = []
# zx_score = []
# bao_score = []
# bian_score = []
# for i in list_result1:
#     temp_zx = []
#     temp_bao = []
#     temp_bian = []
#     temp_zx_score = 0
#     temp_bao_score = 0
#     temp_bian_score = 0
#     for j in range(len(i[2])):
#         if i[2][j] == 0:
#             temp_zx.append(i[0][j])
#             temp_zx_score += i[1][j]
#         elif i[2][j] == 1:
#             temp_bao.append(i[0][j])
#             temp_bao_score += i[1][j]
#         elif i[2][j] ==2:
#             temp_bian.append(i[0][j])
#             temp_bian_score += i[1][j]
#         else:
#             continue
#     zx.append(temp_zx)
#     bao.append(temp_bao)
#     bian.append(temp_bian)
#     zx_score.append(temp_zx_score)
#     bao_score.append(temp_bao_score)
#     bian_score.append(temp_bian_score)
# 
# #将得分结果输出为xlsx和pickle文件
# score = [zx, zx_score, bao, bao_score, bian, bian_score]
# df_score = pd.DataFrame(np.array(score).T)
# df_score.columns = ['中性词','中性词得分','褒义词','褒义词得分','贬义词','贬义词得分']
# df_score.to_pickle(path+'dc_score')
# df_score.to_excel(path+'dc_score.xlsx', index=False)
# #df_score.to_pickle(path+'fs_score')
# #df_score.to_excel(path+'fs_score.xlsx', index=False)
# =============================================================================


# =============================================================================
# '''第三部分：词云绘制，分布图，平均分'''
# #读取所需数据并进行处理
# data = pd.read_pickle(path+'dc_score')
# #data = pd.read_pickle(path+'fs_score')
# word1 = data.iloc[:, [0,2,4]]
# score1 = data.iloc[:, [1,3,5]]
# 
# #计算平均分并进行输出
# mean1 = np.mean(score1, axis = 0)
# df_mean = pd.DataFrame(mean1.reshape(-1,3), columns=['中性词均分','褒义词均分','贬义词均分'],
#                     index=[filenames[0][:3]])
# df_mean.to_excel(path+'dc_mean.xlsx')
# #df_mean.to_excel(path+'fs_mean.xlsx')
# 
# ###汇总词语并统计频数
# word_zx_all = []
# for i in word1.iloc[:,0]:
#     for j in i:
#         if j != '':
#             word_zx_all.append(j)
#         else:
#             continue
# df_word_zx_all = pd.DataFrame(word_zx_all)
# word_zx_fre = df_word_zx_all.iloc[:,0].value_counts()
# 
# 
# word_bao_all = []
# for i in word1.iloc[:,1]:
#     for j in i:
#         if j != '':
#             word_bao_all.append(j)
#         else:
#             continue
# df_word_bao_all = pd.DataFrame(word_bao_all)
# word_bao_fre = df_word_bao_all.iloc[:,0].value_counts()
# 
# 
# word_bian_all = []
# for i in word1.iloc[:,2]:
#     for j in i:
#         if j != '':
#             word_bian_all.append(j)
#         else:
#             continue
# df_word_bian_all = pd.DataFrame(word_bian_all)
# word_bian_fre = df_word_bian_all.iloc[:,0].value_counts()
# 
# #输出excel表格
# list_word_fre = [word_zx_fre.index.tolist(), word_zx_fre.values.tolist(),
#                  word_bao_fre.index.tolist(), word_bao_fre.values.tolist(),
#                  word_bian_fre.index.tolist(), word_bian_fre.values.tolist()]
# df_word_fre = pd.DataFrame(list_word_fre)
# df_word_fre = pd.DataFrame(np.array(df_word_fre).T)
# df_word_fre.columns = ['中性词','中性词频数','褒义词','褒义词频数','贬义词','贬义词频数']
# df_word_fre.to_excel(path+'dc_frequence.xlsx', index = False)
# #df_word_fre.to_excel(path+'fs_frequence.xlsx', index = False)
# =============================================================================


#设置显示中文
import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['font.family']='sans-serif'
mpl.rcParams['font.size'] = 10

###绘制分布图
#读取删去了“通过”和“骄傲”的excel
df_word_fre = pd.read_excel(path+'dc_frequence.xlsx')
#df_word_fre = pd.read_excel(path+'fs_frequence.xlsx')

plt.bar(df_word_fre.iloc[:15,0],df_word_fre.iloc[:15,1])
plt.savefig(path+'词频分布图\\dc中性.png')
#plt.savefig(path+'词频分布图\\fs中性.png')
plt.show()

plt.bar(df_word_fre.iloc[:15,2],df_word_fre.iloc[:15,3])
plt.savefig(path+'词频分布图\\dc褒义.png')
#plt.savefig(path+'词频分布图\\fs褒义.png')
plt.show()

plt.bar(df_word_fre.iloc[:15,4],df_word_fre.iloc[:15,5])
plt.savefig(path+'词频分布图\\dc贬义.png')
#plt.savefig(path+'词频分布图\\fs贬义.png')
plt.show()



###绘制词云
backgroud_Image = plt.imread(path + '词云\\词云1.jpg')
wc = WordCloud(font_path='simhei.ttf',background_color='white', max_words=500, mask=backgroud_Image)

dict_word_zx = dict(zip(df_word_fre['中性词'].values[:500],df_word_fre['中性词频数'].values[:500]))
wc.generate_from_frequencies(dict_word_zx)
plt.imshow(wc)
plt.axis("off")
plt.savefig(path+'词云\\dc中性.png', dpi=1000)
#plt.savefig(path+'词云\\fs中性.png', dpi=1000)
plt.show()


dict_word_bao = dict(zip(df_word_fre['褒义词'].values[:500],df_word_fre['褒义词频数'].values[:500]))
wc.generate_from_frequencies(dict_word_bao,)
plt.imshow(wc)
plt.axis("off")
plt.savefig(path+'词云\\dc褒义.png', dpi=1000)
#plt.savefig(path+'词云\\fs褒义.png', dpi=1000)
plt.show()


dict_word_bian = dict(zip(df_word_fre['贬义词'].values[:500],df_word_fre['贬义词频数'].values[:500]))
wc.generate_from_frequencies(dict_word_bian,)
plt.imshow(wc)
plt.axis("off")
plt.savefig(path+'词云\\dc贬义.png', dpi=1000)
#plt.savefig(path+'词云\\fs贬义.png', dpi=1000)
plt.show()































