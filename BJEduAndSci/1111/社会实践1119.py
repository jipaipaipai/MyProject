# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 09:06:30 2018

@author: haoyu
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

path = 'D:\\软件\\微信\\文件\\WeChat Files\\liuhaoyun123456\\Files\\项目\\北京教科院\\社会实践\\1111\\'
filenames = os.listdir(path+'数据/')

#data = pd.read_excel(path+'数据/'+filenames[0])
#data = pd.read_excel(path+'数据/'+filenames[2])

#数据处理
df1 = pd.read_pickle(path+'数据/'+filenames[1])#房山
df1 = df1.iloc[:,[2,12]]
df2 = pd.read_excel(path+'数据/'+filenames[3])
df2 = df2.iloc[:,[2,6]]
data = pd.merge(df1, df2, how='left', left_on=u'学校名称',right_on=u'学校名称')

zzx = data[data['学校所在地域']=='镇中心区']
cz = data[data['学校所在地域']=='村庄']
cxjhq = data[data['学校所在地域']=='城乡结合区']
zcq = data[data['学校所在地域']=='主城区']

#地点分布
zzx_dis = zzx.iloc[:,1].value_counts()
cz_dis = cz.iloc[:,1].value_counts()
cxjhq_dis = cxjhq.iloc[:,1].value_counts()
zcq_dis = zcq.iloc[:,1].value_counts()

# =============================================================================
# #输出为xlsx
# out = pd.DataFrame({'zzx':zzx_dis.index,'zzx_dis':zzx_dis.values})
# for i in [cz_dis,cxjhq_dis,zcq_dis]:
#     temp = pd.DataFrame({1:i.index,2:i.values})
#     out = pd.concat([out,temp], axis=1, ignore_index=True)
# out.columns = ['zzx','zzx_dis','cz','cz_dis','cxjhq','cxjhq_dis','zcq','zcq_dis']
# out.to_excel(path+'frequence_dis.xlsx')
# =============================================================================


#设置绘制函数参数
import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['font.family']='sans-serif'
mpl.rcParams['font.size'] = 5

#开始绘制
from wordcloud import WordCloud

#镇中心
backgroud_Image = plt.imread(path + '词云\\词云1.jpg')
wc = WordCloud(font_path='simhei.ttf',background_color='white', max_words=500, mask=backgroud_Image)
dict_zzx_dis = dict(zip(zzx_dis.index,zzx_dis.values))
wc.generate_from_frequencies(dict_zzx_dis)
plt.imshow(wc)
plt.axis("off")
plt.savefig(path+'词云\\zzx.png', dpi=1000)
plt.show()

#村庄
backgroud_Image = plt.imread(path + '词云\词云3.jpg')
wc = WordCloud(font_path='simhei.ttf',background_color='white', max_words=500, mask=backgroud_Image)
dict_cz_dis = dict(zip(cz_dis.index,cz_dis.values))
wc.generate_from_frequencies(dict_cz_dis)
plt.imshow(wc)
plt.axis("off")
plt.savefig(path+'词云\cz.png', dpi=1000)
plt.show()

#城乡结合区
backgroud_Image = plt.imread(path + '词云\词云4.jpg')
wc = WordCloud(font_path='simhei.ttf',background_color='white', max_words=500, mask=backgroud_Image)
dict_cxjhq_dis = dict(zip(cxjhq_dis.index,cxjhq_dis.values))
wc.generate_from_frequencies(dict_cxjhq_dis)
plt.imshow(wc)
plt.axis("off")
plt.savefig(path+'词云\cxjhq.png', dpi=1000)
plt.show()

#主城区
backgroud_Image = plt.imread(path + '词云\词云5.jpg')
wc = WordCloud(font_path='simhei.ttf',background_color='white', max_words=500, mask=backgroud_Image)
dict_zcq_dis = dict(zip(zcq_dis.index,zcq_dis.values))
wc.generate_from_frequencies(dict_zcq_dis)
plt.imshow(wc)
plt.axis("off")
plt.savefig(path+'词云\zcq.png', dpi=1000)
plt.show()






























