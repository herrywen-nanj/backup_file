#!/usr/bin/python
# - * - coding: utf-8 - * -
filename = '1.txt'
try:
    with open(filename) as file_object:
      t = file_object.read()
except FileNotFoundError:
    print 'you have' + filename + "is not exist!"
else:
    words = t.split()
    #print的两种写法，可以带逗号，后面直接跟参数值。也可以不带逗号，后面直接跟%参数值
    print 'danci de geshi yigong shi %d'  %len(words)
    #print 'danci de geshi yigong shi' , len(words)
