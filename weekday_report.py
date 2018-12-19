#!/usr/bin/python
# - * - coding: utf-8 - * -
#作用：写周报
import datetime
filename = '1.txt'
string_date = '%Y年-%m月-%d日'
weekdate = []
raw_content = []
def getYesterday(): 
   """ 获取一周每天的时间戳且格式化 """
    today=datetime.date.today()
    #weekdate.append(today)
    for i in range(0,5):
     oneday=datetime.timedelta(days=i)
     yesterday=today-oneday
     yesterday = yesterday.strftime(string_date)  
     weekdate.append(yesterday)

getYesterday()
weekdate.reverse()


def get_rawcontent():
    """ 获取周报内容 """
 j = 0
 while j< 5:
  content = raw_input("please input you content: ")
  raw_content.append(content)
  j += 1
get_rawcontent()

def get_report():
    """ 整合内容 """
 for i in range(0,5):
   count_report = weekdate[i] + ' ' + raw_content[i] + "\n"
   with open(filename,'a') as file_object:
     file_object.write(count_report)
get_report()





