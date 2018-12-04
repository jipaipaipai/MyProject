###############
library(sqldf)

a1r <- head(warpbreaks)
a1s <- sqldf("select * from warpbreaks limit 6")
identical(a1r, a1s)

a2r <- subset(CO2, grepl("^Qn", Plant))
a2s <- sqldf("select * from CO2 where Plant like 'Qn%'")
all.equal(as.data.frame(a2r), a2s)

a3<-warpbreaks
id<-c('A','B')
name<-c('学生1','学生2')
cl<-data.frame(id,name)
sqldf("select name, count(wool) as count from a3 inner join cl on a3.wool=cl.id group by name")
sqldf("select wool, count(wool) aS sum from a3 inner join cl where wool=id group by name")



###############
library(sqldf)
setwd('D:/软件/微信/文件/WeChat Files/liuhaoyun123456/Files/项目/北京教科院/社会实践活动2017-2018学年学生提交感受情况20180805/')
filename<-dir('D:/软件/微信/文件/WeChat Files/liuhaoyun123456/Files/项目/北京教科院/社会实践活动2017-2018学年学生提交感受情况20180805/')

stu<-openxlsx::read.xlsx(filename[19])
sch<-openxlsx::read.xlsx(filename[20])

f1<-openxlsx::read.xlsx(filename[1])
f2<-openxlsx::read.xlsx(filename[8])
f<-rbind(f1,f2)
save(f,file='D:/软件/微信/文件/WeChat Files/liuhaoyun123456/Files/项目/北京教科院/example.Rdata')
load('D:/软件/微信/文件/WeChat Files/liuhaoyun123456/Files/项目/北京教科院/example.Rdata')

stu1<-stu[,c(4,6,7,9)]
stu.inf<-sqldf("select f.教育ID as ID, count(f.教育ID) as num,stu.姓名 as name,
                stu.性别 as sex,stu.年级 as grade,stu.区 as area,stu.学校名称 as sch,
                sch.学校代码 as schcode
                from f inner join stu on f.教育ID=stu.教育ID号,sch on f.学校名称=sch.学校名称
                group by 姓名")
stu.inf[,2]<-stu.inf[,2]/2
stu.inf$grade<-factor(stu.inf$grade)
stu.inf$sex<-factor(stu.inf$sex)

###############
##学生参加次数分布
count<-as.vector(matrix(0,70,1))
for(i in 1:length(stu.inf$num)){
  count[stu.inf$num[i]] = count[stu.inf$num[i]]+1

}
count<-data.frame(infs=1:70,num=count)
count<-count[-which(count$num==0),]
count$infs<-as.numeric(count$infs)
avg<-sum(as.numeric(count$infs)*count$num)/sum(count$num)
pct<-count['10',2]/sum(count$num)
barplot(count$num)

##年级分布
grade<-fct_count(stu.inf$grade)
barplot(grade$n,legend.text = grade$f,col = grade$n)

##
aaa<-stu.inf$sch
aaa<-factor(aaa)
aaaa<-fct_count(aaa)
aaaa<-as.vector(aaaa)
barplot(aaaa$n)
mean(aaaa$n)
bbbb<-aaaa[which(aaaa$n>350),]
bbbb<-as.vector(bbbb)
barplot(bbbb$n)

##活动类别分布
act<-f$活动分类
faca<-factor(act)
counta<-fct_count(faca)
barplot(counta$n)

###############
###将学校和类别分别分开
load('D:/软件/微信/文件/WeChat Files/liuhaoyun123456/Files/项目/北京教科院/example.Rdata')
act_sch_name<-names(table(f['学校名称']))
act_cat_name<-names(table(f['活动分类']))
act_sch_list<-list()
act_cat_list<-list()
for(i in 1:length(act_sch_name)){
  act_sch_list[[i]]<-f[which(f['学校名称']==act_sch_name[i]),]
}
for(i in 1:length(act_cat_name)){
  act_cat_list[[i]]<-f[which(f['活动分类']==act_cat_name[i]),]
}

###进行分词
library(jiebaR)
library(stringr)
wordseg<-worker(stop_word ='D:/软件/微信/文件/WeChat Files/liuhaoyun123456/Files/项目/北京教科院/stopword.txt' )
word_sch<-list()
word_cat<-list()
for(i in 1:length(act_sch_name)){
  word_sch[[i]]<-segment(act_sch_list[[i]][,7],wordseg)
}
for(i in 1:length(act_cat_name)){
  word_cat[[i]]<-segment(act_cat_list[[i]][,7],wordseg)
}
IDF_wordseg<-worker('keywords',topn=50)
all_sch<-paste(act_sch_list[[2]][,7],collapse = '')
all_sch<-str_replace(all_sch,' |,','')
IDF_sch<-IDF_wordseg<=all_sch
IDF_sch<-data.frame(score=names(IDF_sch),word=IDF_sch)

##活动类型频数分布，描述，不同类型次数，提取地点
