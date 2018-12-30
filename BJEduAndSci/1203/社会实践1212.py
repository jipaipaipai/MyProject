# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 16:45:52 2018

@author: haoyu
"""

# =============================================================================
# '''将活动名称的分词结果输出为excel'''
# 
# import numpy as np
# import pandas as pd
# import jieba
# 
# path = r'D:\软件\微信\文件\WeChat Files\liuhaoyun123456\Files\项目\北京教科院\社会实践\1203\\'
# data = pd.read_pickle(path+'数据\\'+'all.pickle')
# 
# place = data['活动名称'].tolist()
# 
# #将数字转化为字符串
# for i in range(len(place)):
#     if type(place[i]) == int or type(place[i]) == float:
#         place[i] = str(place[i])
# 
# #进行分词
# place_cuts = []
# for i in place:
#     place_cuts.append(jieba.lcut(i))
# 
# place_cuts_df = pd.DataFrame(np.array(place_cuts))
# 
# place_cuts_df.to_excel(path+'cut_result.xlsx')
# =============================================================================


# =============================================================================
# '''制作报告表格'''
# import numpy as np
# import pandas as pd
# import os
# 
# path = r'D:\软件\微信\文件\WeChat Files\liuhaoyun123456\Files\项目\北京教科院\社会实践\1203\\'
# filenames2 = os.listdir(path+'数据\\')
# 
# ##各年级人数
# grade = pd.DataFrame()
# for i in filenames2[1:]:
#     temp = pd.read_pickle(path+'数据\\'+i)
#     temp_grade = pd.DataFrame(temp['年级'].value_counts())
#     temp_grade.columns = [i[:-7]]
#     grade = pd.concat([grade,temp_grade],axis=1)
# grade = grade.iloc[1:,:]
# grade = grade.T
# grade.to_excel(path+'grade.xlsx')
# 
# #合并所有文件
# all_data = pd.DataFrame()
# for i in filenames2[1:]:
#     temp = pd.read_pickle(path+'数据\\'+i)
#     all_data = pd.concat([all_data,temp])
# 
# dup_data = all_data.drop_duplicates('学生姓名')
# 
# ##全市，团体，个人的主题人数和人次
# #全市
# counts_city = all_data['考核类型'].value_counts()
# count_city = dup_data['考核类型'].value_counts()
# 
# #团体
# team_all_data = all_data[all_data['活动类型']=='团体预约']
# team_dup_data = dup_data[dup_data['活动类型']=='团体预约']
# counts_team = team_all_data['考核类型'].value_counts()
# count_team = team_dup_data['考核类型'].value_counts()
# 
# #个人
# single_all_data = all_data[all_data['活动类型']=='自主选课']
# single_dup_data = dup_data[dup_data['活动类型']=='自主选课']
# counts_single = single_all_data['考核类型'].value_counts()
# count_single = single_dup_data['考核类型'].value_counts()
# 
# #输出表格
# out = pd.DataFrame({'全市人数':count_city,'个人人数':count_single,'团体人数':count_team,
#                    '全市人次':counts_city,'个人人次':counts_single,'团体人次':counts_team})
# out.to_excel(path+'主题人次.xlsx')
# 
# ##各个主题的人数
# #总数
# theme = pd.DataFrame()
# for i in filenames2[1:]:
#     temp = pd.read_pickle(path+'数据\\'+i)
#     temp_theme = pd.DataFrame(temp['考核类型'].value_counts(True))
#     temp_theme.columns = [i[:-7]]
#     theme = pd.concat([theme,temp_theme],axis=1)
# theme.to_excel(path+'theme.xlsx')
# 
# ##团体
# theme_team = pd.DataFrame()
# for i in filenames2[1:]:
#     temp = pd.read_pickle(path+'数据\\'+i)
#     temp = temp[temp['活动类型']=='团体预约']
#     temp_theme = pd.DataFrame(temp['考核类型'].value_counts())
#     temp_theme.columns = [i[:-7]]
#     theme_team = pd.concat([theme_team,temp_theme],axis=1)
# theme_team.to_excel(path+'theme_team.xlsx')
# 
# ##个人
# theme_single = pd.DataFrame()
# for i in filenames2[1:]:
#     temp = pd.read_pickle(path+'数据\\'+i)
#     temp = temp[temp['活动类型']=='自主选课']
#     temp_theme = pd.DataFrame(temp['考核类型'].value_counts())
#     temp_theme.columns = [i[:-7]]
#     theme_single = pd.concat([theme_single,temp_theme],axis=1)
# theme_single.to_excel(path+'theme_single.xlsx')
# =============================================================================



# =============================================================================
# 
# '''活动主题和活动感受'''
# ##褒义贬义中性词频和得分
# import numpy as np
# import pandas as pd
# 
# path = r'D:\软件\微信\文件\WeChat Files\liuhaoyun123456\Files\项目\北京教科院\社会实践\1203\\'
# data = pd.read_pickle(path+'emotion_score.pickle')
# zx_word = data['中性词'].tolist()
# bao_word = data['褒义词'].tolist()
# bian_word = data['贬义词'].tolist()
# 
# zx_fre = []
# bao_fre = []
# bian_fre = []
# for i, j, k in zip(zx_word, bao_word, bian_word):
#     zx_fre.append(len(i))
#     bao_fre.append(len(j))
#     bian_fre.append(len(k))
# zong_fre = np.array(zx_fre) + np.array(bao_fre) + np.array(bian_fre)
# zong_fre = zong_fre.tolist()
# fre = pd.DataFrame(np.array([zx_fre,bao_fre,bian_fre,zong_fre]).T)
# fre.columns = ['中性词词频','褒义词词频','贬义词词频','总词频']
# out = pd.concat([data,fre],axis=1)
# out.to_excel(path+'score.xlsx')
# out.to_pickle(path+'score.pickle')
# 
# ##活动名称词云
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import jieba
# from wordcloud import WordCloud
# 
# path = r'D:\软件\微信\文件\WeChat Files\liuhaoyun123456\Files\项目\北京教科院\社会实践\1203\\'
# data = pd.read_pickle(path+'数据\\'+'all.pickle')
# team_name = data[data['活动类型']=='团体预约']['活动名称'].tolist()
# single_name = data[data['活动类型']=='自主选课']['活动名称'].tolist()
# 
# team_name = [str(i) for i in team_name]
# single_name = [str(i) for i in single_name]
# 
# team_name_word = ''.join(team_name)
# single_name_word = ''.join(single_name)
# 
# seg_team = jieba.lcut(team_name_word)
# seg_single = jieba.lcut(single_name_word)
# 
# backgroud_Image = plt.imread(path + '词云\\词云5.jpg')
# wc = WordCloud(font_path='simhei.ttf',background_color='white', max_words=500, mask=backgroud_Image)
# wc.generate(' '.join(seg_team))
# plt.imshow(wc)
# plt.axis("off")
# plt.savefig(path+'词云\\团体活动名称.png', dpi=1000)
# plt.show()
# 
# backgroud_Image = plt.imread(path + '词云\\词云5.jpg')
# wc = WordCloud(font_path='simhei.ttf',background_color='white', max_words=500, mask=backgroud_Image)
# wc.generate(' '.join(seg_single))
# plt.imshow(wc)
# plt.axis("off")
# plt.savefig(path+'词云\\自主活动名称.png', dpi=1000)
# plt.show()
# =============================================================================



























