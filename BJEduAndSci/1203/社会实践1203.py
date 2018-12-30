# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 10:31:57 2018

@author: haoyu
"""

import numpy as np
import pandas as pd
import os
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# =============================================================================
# '''数据预处理'''
# #将所有区的数据读入并存为pickle文件
# path1 = r'D:\软件\微信\文件\WeChat Files\liuhaoyun123456\Files\项目\北京教科院\\'
# path = r'D:\软件\微信\文件\WeChat Files\liuhaoyun123456\Files\项目\北京教科院\社会实践\1203\\'
# filenames = os.listdir(r'D:\软件\微信\文件\WeChat Files\liuhaoyun123456\Files\项目\北京教科院\数据')
# 
# for i in filenames:
#     temp = pd.read_excel(path1+'数据\\'+i)
#     temp.to_pickle(path+'数据\\'+i[0:-5]+'.pickle')
# 
# #每个区抽取8000个数据进行合并,并输出pickle和xlsx文件
# filenames2 = os.listdir(path+'数据\\')
# data1 = []
# for i in filenames2:
#     temp = pd.read_pickle(path+'数据\\'+i)
#     rows = np.random.randint(1,len(temp.iloc[:,0]),8000)
#     temp2 = temp.iloc[rows,:]
#     data1.append(temp2)
# 
# data = pd.DataFrame(data1[0])
# for i in data1[1:]:
#     data = pd.concat([data,i])
# 
# data.to_pickle(path+'数据\\'+'all.pickle')
# data.to_excel(path1+'数据\\'+'all.xlsx')
# =============================================================================


# =============================================================================
# #活动分布图
# data = pd.read_pickle(path+'fs')
# name_act = data.活动名称.tolist()
# name_sch = data.学校名称.tolist()
# name_gro = data.活动类型.tolist()
# name_cat = data.考核类型.tolist()
# 
# 
# #活动区县统计
# act_loc = data['活动区县'].value_counts()
# 
# import matplotlib as mpl
# mpl.rcParams['font.sans-serif'] = ['SimHei']
# mpl.rcParams['font.family']='sans-serif'
# mpl.rcParams['font.size'] = 6
# 
# 
# x=np.arange(len(act_loc))+1 #设置y轴的数值，需将numbers列的数据先转化为数列，再转化为矩阵格式
# y=np.array(list(act_loc))
# xticks1=list(act_loc.index) #构造不同课程类目的数列
# plt.bar(x,y,width = 0.35,align='center',color = 'c',alpha=0.8)#画出柱状图
# #设置x轴的刻度，将构建的xticks代入，同时由于课程类目文字较多，在一块会比较拥挤和重叠，因此设置字体和对齐方式
# plt.xticks(x,xticks1,size='small',rotation=30)
# plt.title('活动区县分布')
# for a,b in zip(range(18), act_loc):
#     plt.text(a+1, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=6)
# plt.savefig(path+'fs活动区县分布'+'.png',dpi=1000)
# plt.show()
# 
# 
# 
# #活动地点统计
# act_area = data['活动地点'].value_counts()
# act_area = act_area[:25]
# 
# import matplotlib as mpl
# mpl.rcParams['font.sans-serif'] = ['SimHei']
# mpl.rcParams['font.family']='sans-serif'
# mpl.rcParams['font.size'] = 5
# 
# 
# x=np.arange(len(act_area))+1 #设置y轴的数值，需将numbers列的数据先转化为数列，再转化为矩阵格式
# y=np.array(list(act_area))
# xticks1=list(act_area.index) #构造不同课程类目的数列
# plt.bar(x,y,width = 0.35,align='center',color = 'c',alpha=0.8)#画出柱状图
# #设置x轴的刻度，将构建的xticks代入，同时由于课程类目文字较多，在一块会比较拥挤和重叠，因此设置字体和对齐方式
# plt.xticks(x,xticks1,size='small',rotation=60)
# plt.title('活动地点分布')
# for a,b in zip(range(len(act_area)), act_area):
#     plt.text(a+1, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=5)
# plt.savefig(path+'fs活动地点分布'+'.png',dpi=1000)
# plt.show()
# =============================================================================


# =============================================================================
# '''第一部分：提取情感词'''
# import jieba
# #读取所需文件
# path = r'D:\软件\微信\文件\WeChat Files\liuhaoyun123456\Files\项目\北京教科院\社会实践\1203\\'
# filenames = os.listdir(path+'数据\\')
# dc = pd.read_pickle(path+'数据\\'+filenames[0])
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
# df_result.to_pickle(path+'emotion.pickle')
# df_result.to_excel(path+'emotion.xlsx')
# #df_result.to_pickle(path+'fs_qgc')
# #df_result.to_excel(path+'fs_qgc.xlsx')
# =============================================================================


# =============================================================================
# '''第二部分：情感词分类并计算得分'''
# #读取并清洗分类完的数据
# df_result1 = pd.read_pickle(path+'emotion.pickle')
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
# df_score.to_pickle(path+'emotion_score.pickle')
# df_score.to_excel(path+'emotion_score.xlsx', index=False)
# #df_score.to_pickle(path+'fs_score')
# #df_score.to_excel(path+'fs_score.xlsx', index=False)
# =============================================================================


# =============================================================================
# '''第三部分：词云绘制，分布图，平均分'''
# #读取所需数据并进行处理
# data = pd.read_pickle(path+'emotion_score.pickle')
# #data = pd.read_pickle(path+'fs_score')
# word1 = data.iloc[:, [0,2,4]]
# score1 = data.iloc[:, [1,3,5]]
# 
# #计算平均分并进行输出
# mean1 = np.mean(score1, axis = 0)
# df_mean = pd.DataFrame(mean1.reshape(-1,3), columns=['中性词均分','褒义词均分','贬义词均分'],
#                     index=[filenames[0][:3]])
# df_mean.to_excel(path+'emotion_mean.xlsx')
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
# df_word_fre.to_excel(path+'emotion_frequence.xlsx', index = False)
# #df_word_fre.to_excel(path+'fs_frequence.xlsx', index = False)
# 
# 
# #设置显示中文
# import matplotlib as mpl
# import matplotlib.pyplot as plt
# mpl.rcParams['font.sans-serif'] = ['SimHei']
# mpl.rcParams['font.family']='sans-serif'
# mpl.rcParams['font.size'] = 10
# 
# ###绘制分布图
# #读取删去了“通过”和“骄傲”的excel
# df_word_fre = pd.read_excel(path+'emotion_frequence.xlsx')
# #df_word_fre = pd.read_excel(path+'fs_frequence.xlsx')
# 
# plt.bar(df_word_fre.iloc[:15,0],df_word_fre.iloc[:15,1])
# plt.savefig(path+'词频分布图\\中性.png',dpi=1000)
# #plt.savefig(path+'词频分布图\\fs中性.png')
# plt.show()
# 
# plt.bar(df_word_fre.iloc[:15,2],df_word_fre.iloc[:15,3])
# plt.savefig(path+'词频分布图\\褒义.png',dpi=1000)
# #plt.savefig(path+'词频分布图\\fs褒义.png')
# plt.show()
# 
# plt.bar(df_word_fre.iloc[:15,4],df_word_fre.iloc[:15,5])
# plt.savefig(path+'词频分布图\\贬义.png',dpi=1000)
# #plt.savefig(path+'词频分布图\\fs贬义.png')
# plt.show()
# 
# 
# 
# ###绘制词云
# from wordcloud import WordCloud
# backgroud_Image = plt.imread(path + '词云\\词云1.jpg')
# wc = WordCloud(font_path='simhei.ttf',background_color='white', max_words=500, mask=backgroud_Image)
# 
# dict_word_zx = dict(zip(df_word_fre['中性词'].values[:500],df_word_fre['中性词频数'].values[:500]))
# wc.generate_from_frequencies(dict_word_zx)
# plt.imshow(wc)
# plt.axis("off")
# plt.savefig(path+'词云\\中性.png', dpi=1000)
# #plt.savefig(path+'词云\\fs中性.png', dpi=1000)
# plt.show()
# 
# 
# dict_word_bao = dict(zip(df_word_fre['褒义词'].values[:500],df_word_fre['褒义词频数'].values[:500]))
# wc.generate_from_frequencies(dict_word_bao,)
# plt.imshow(wc)
# plt.axis("off")
# plt.savefig(path+'词云\\褒义.png', dpi=1000)
# #plt.savefig(path+'词云\\fs褒义.png', dpi=1000)
# plt.show()
# 
# 
# dict_word_bian = dict(zip(df_word_fre['贬义词'].values[:500],df_word_fre['贬义词频数'].values[:500]))
# wc.generate_from_frequencies(dict_word_bian,)
# plt.imshow(wc)
# plt.axis("off")
# plt.savefig(path+'词云\\贬义.png', dpi=1000)
# #plt.savefig(path+'词云\\fs贬义.png', dpi=1000)
# plt.show()
# =============================================================================



































