#####
#读取合并文件以及分区
load('D:/软件/微信/文件/WeChat Files/liuhaoyun123456/Files/项目/北京教科院/example.Rdata')
dc_all<-data.frame(f[f[2]=='东城区',])
fs_all<-data.frame(f[f[2]=='房山区',])


########先以东城区为例
#去除活动名称重复的行
dc<-dc_all[!duplicated(dc_all$活动名称), ]
fs<-fs_all[!duplicated(fs_all$活动名称), ]

#提取32个活动类型名称以及学校名称
act_name<-names(table(dc['活动分类']))
cat_name<-names(table(dc['活动类型']))
sch_name<-names(table(dc['学校名称']))

#按照活动分类，将活动名称整合
word_act_list<-list()
for(i in 1:length(act_name)){
  word_act_list[[i]]<-dc[which(dc['活动分类']==act_name[i]),'活动名称']
}

#####
#####对各个活动分类进行分词
library(jiebaR)
library(stringr)
#先整合跑，筛除无用词
wordseg<-worker('keywords',topn=30)
#wordseg<-worker('mp',topn=30)
a<-c()
for(i in 1:32){a<-cbind(a,paste(word_act_list[[i]],collapse = ''))}
b<-paste(a,collapse = '')
word_all<-data.frame(word=wordseg<=b,score=names(wordseg<=b),stringsAsFactors = F)

#分类分词
word_act<-data.frame(matrix(NA,30,32))
for(i in 1:32){
  a<-paste(word_act_list[[i]],collapse = '')
  b<-wordseg<=a
  word_act[,i]<-b
}
colnames(word_act)<-act_name


#####
#按照类型分类，将活动名称整合
word_cat_list<-list()
for(i in 1:length(act_name)){
  word_cat_list[[i]]<-dc[which(dc['活动类型']==cat_name[i]),'活动名称']
}

#分词
word_cat<-data.frame(matrix(NA,30,2))
for(i in 1:2){
  a<-paste(word_cat_list[[i]],collapse = '')
  b<-wordseg<=a
  word_cat[,i]<-b
}
colnames(word_cat)<-cat_name


#####
#按照学校分类，将活动名称整合
word_sch_list<-list()
for(i in 1:length(sch_name)){
  word_sch_list[[i]]<-dc[which(dc['学校名称']==sch_name[i]),'活动名称']
}

#分词
word_sch<-data.frame(matrix(NA,30,length(sch_name)))
for(i in 1:length(sch_name)){
  a<-paste(word_sch_list[[i]],collapse = '')
  b<-wordseg<=a
  word_sch[,i]<-b
}
colnames(word_cat)<-cat_name

##输出表格
output<-data.frame(word_cat,a=1:30,word_act,a=1:30,word_sch)
write.csv(output,file='D:/软件/微信/文件/WeChat Files/liuhaoyun123456/Files/项目/北京教科院/compare.csv')

#####






