#!/usr/bin/python
# - * - coding: utf-8 - * -
#作用，分别计算每个文本的单词数，并且输出所有文本的单词总数
a = []
sum = 0 
def count_words(filename):
#filename = '1.txt'
 try:
  with open(filename) as file_object:
   t = file_object.read()
 except IOError:
  print 'you have' + ' ' + filename + ' is not exist!'
 else:
  words = t.split()
  numbers = len(words)
  a.append(numbers)
    #print的两种写法，可以带逗号，后面直接跟参数值。也可以不带逗号，后面直接跟%参数值
  print 'danci de geshi yigong shi %d'  %numbers
#    #print 'danci de geshi yigong shi' , numbers

filenames = [ '1.txt','2.txt','3.txt' ]
for filename in filenames:
 count_words(filename)

for i in a:
 sum += int(i)
print sum
#两种写法，一个是用sum计数，一个用sum函数，
#sum的参数是一个list，这里a就是list
#print '所有单词总数为' + str(sum(a))
