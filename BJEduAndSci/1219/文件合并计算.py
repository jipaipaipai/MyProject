# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 16:43:32 2018

@author: haoyu
"""

import os
import pandas as pd

path = r'D:\软件\微信\文件\WeChat Files\liuhaoyun123456\Files\项目\北京教科院\社会实践\1219\\'
filenames = os.listdir(path+'数据\\')
data_1 = pd.read_pickle(path+'数据\\all.pickle')
data_1.index = [i for i in range(136000)]
data_2 = pd.read_excel(path+'数据\\'+filenames[2])
data_2.index = [i for i in range(136002)]
out = pd.concat([data_1['区'],data_2.iloc[:-2,:]], axis=1)
out.to_pickle(path+'数据\\encoding.pickle')

group = out.groupby('区')
percent = []
area = []
area_percent = []
for i in group:
    area.append(i[0])
    temp = i[1].iloc[:,6:]
    for j in range(6):
        temp1 = temp.iloc[:,j]
        temp_percent = temp1.value_counts(True)
        temp_percent.columns = temp.columns[j]
        area_percent.append(temp_percent)
    percent.append(area_percent)

out_percent = pd.DataFrame()
for i in range(17):
    temp = pd.DataFrame()
    for j in range(6):
        count = j + i*6
        temp = pd.concat([temp,area_percent[count]],axis=1)
    temp.index = [str(area[i])+str(temp.index[0]),str(area[i])+str(temp.index[1])]
    out_percent = pd.concat([out_percent,temp])
out_percent.to_excel(path+'数据\\'+'area_percent.xlsx')
out_percent.to_pickle(path+'数据\\'+'area_percent.pickle')






























