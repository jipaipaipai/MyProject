
#载入所需要的包
library(data.table)
library(xlsx)

#####################################

##数据处理部分


#数据读取
dcq<-openxlsx::read.xlsx("C:\\Users\\linwei\\Desktop\\社会实践活动2017-2018学年学生提交感受情况20180805\\17个区\\01东城区.xlsx")
student_msg_all<-openxlsx::read.xlsx("C:\\Users\\linwei\\Desktop\\各区初中学生信息.xlsx")
sch_msg_all<-openxlsx::read.xlsx("C:\\Users\\linwei\\Desktop\\各区初中学校信息.xlsx")


#dcq_unique里每个教育ID留一条记录
dcq_unique<-dcq
dcq_unique<-dcq_unique[!duplicated(dcq_unique$"教育ID"),]


#得到每位学生的参与次数
table(dcq$教育ID)
dcq_chishu<-as.data.frame(table(dcq$教育ID))
colnames(dcq_chishu)<-c("教育ID","次数")



#转换成data.table
dcq_uniqueTD<-data.table(dcq_unique)
student_msg_allDT<-data.table(student_msg_all)
sch_msg_allDT<-data.table(sch_msg_all)


#透视表
setkey(sch_msg_allDT,"区")
dcq_sch_msg<-sch_msg_allDT[区=="东城区"]

setkey(student_msg_allDT,"区")
dcq_stdmsg_TD<-student_msg_allDT[区=="东城区",]

#
dcq_sch_msg
aggregate(学生数~学校名称,dcq_sch_msg,sum)


#变量重命名
names(dcq_stdmsg_TD)[9]<-"教育ID"

#数据合并
dcq_merge1<-merge(dcq_uniqueTD,dcq_stdmsg_TD,by="教育ID")

dcq_merge2<-merge(dcq_merge1,dcq_chishu,by="教育ID")

#合并学校人数(没写完)
#dcq_merge3<-merge(dcq_merge2)


colnames(dcq_merge2)

#####################################

###数据分析部分

options(digits=3)

##每个学生参与次数的描述统计

#平均数
mean(dcq_merge2$次数)
#百分数
cishufenbuTB<-table(dcq_merge2$次数)
cishufenbuTB
prop.table(cishufenbuTB)*100




##平均参与次数

#学校分布
dcq_xuexiao_cishu<-aggregate(次数~学校名称.x,dcq_merge2,mean)
dcq_xuexiao_cishu<-dcq_xuexiao_cishu[order(-dcq_xuexiao_cishu$次数),]
dcq_xuexiao_cishu#北京市第一一五中学 6.83次 最低
range(dcq_xuexiao_cishu$次数)

#年级分布
dcq_nianji_cishu<-aggregate(次数~年级,dcq_merge2,mean)
dcq_nianji_cishu<-dcq_nianji_cishu[order(-dcq_nianji_cishu$次数),]
dcq_nianji_cishu



#所有学生参加活动主题上的分布情况。   
dcq_huodongfenlei<-as.data.frame(table(dcq_cbind1$活动分类))
order_dcq_huodongfenlei_all<-dcq_huodongfenlei[order(-dcq_huodongfenlei$Freq),]
order_dcq_huodongfenlei_all1<-cbind(order_dcq_huodongfenlei_all,(order_dcq_huodongfenlei_all$Freq)*100/sum(order_dcq_huodongfenlei_all$Freq))
names(order_dcq_huodongfenlei_all1)[1]<-"活动分类"
names(order_dcq_huodongfenlei_all1)[2]<-"参与次数"
names(order_dcq_huodongfenlei_all1)[3]<-"百分比"





##各活动类型平均参与次数(还没改)
all1<-rep(1,nrow(dcq))
dcq_cbind1<-cbind(dcq,all1)

#总的分布
aggregate(all1~活动类型,dcq_cbind1,sum)

#学校分布
dcq_xuexiao_huodongfenlei1<-aggregate(all1~学校名称+活动分类,dcq_cbind1,sum)
dcq_xuexiao_huodongfenlei1
sdata1=split(dcq_xuexiao_huodongfenlei1,dcq_xuexiao_huodongfenlei1$学校名称)
order_huodongfenlei1=lapply(sdata1,function(x) x[order(-x[,3]),])

dcq_xuexiao_huodongfenlei2<-aggregate(all1~活动分类+学校名称,dcq_cbind1,sum)
dcq_xuexiao_huodongfenlei2
sdata2=split(dcq_xuexiao_huodongfenlei2,dcq_xuexiao_huodongfenlei2$活动分类)
order_huodongfenlei2=lapply(sdata2,function(x) x[order(-x[,3]),])


dcq_xuexiao_huodongmingcheng1<-aggregate(all1~活动名称+学校名称,dcq_cbind1,sum)
dcq_xuexiao_huodongmingcheng1
sdata3=split(dcq_xuexiao_huodongmingcheng1,dcq_xuexiao_huodongmingcheng1$活动名称)
order_huodongmingcheng1=lapply(sdata3,function(x) x[order(-x[,3]),])
#order_huodongmingcheng1意义不明显

dcq_xuexiao_huodongmingcheng2<-aggregate(all1~学校名称+活动名称,dcq_cbind1,sum)
dcq_xuexiao_huodongmingcheng2
sdata4=split(dcq_xuexiao_huodongmingcheng2,dcq_xuexiao_huodongmingcheng2$学校名称)
order_huodongmingcheng2=lapply(sdata4,function(x) x[order(-x[,3]),])



#####################################


#年级分布
#dcq_xuexiao_zhuti<-aggregate(all1~活动分类+学校名称,dcq_cbind1,sum)
#aggregate(all1~活动类型,dcq_cbind1,sum)
#aggregate(all1~活动类型+年级,dcq_cbind1,sum)


























#dcq_nianji<-dcq_stdmsg_TD[,c("教育ID","年级")]
#dcq_qinggan<-merge(dcq,dcq_nianji,by="教育ID")











##分类汇总

#学校名称
# dcq_merge_1<-dcq_merge[,.N,by="学校名称.x"]
# dcq_merge_1<-dcq_merge_1[order(-dcq_merge_1$N),]
# dcq_merge_1
#这里的值是这个学校有多少人 参与过 实践活动(不是次数)

#年级
#dcq_merge2[,.N,by="年级"]
#这里的值是这个学校有多少人 参与过 实践活动(不是次数)

# #活动分类
# dcq_merge_3<-dcq_merge[,.N,by="活动分类"]
# dcq_merge_3<-dcq_merge_3[order(-dcq_merge_3$N),]
# dcq_merge_3
# 错误，因为前面每个人只取了一次的活动信息



