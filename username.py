#!/usr/bin/python
#不断地获取用户名的输入，并且保存在本地文件中，每行一个
print 'Enter exit or q to quit'
def get_input():
   filename = 'username.txt'
   while True:
    username = raw_input("please input your name:")
    if username == 'exit' or username == 'q':
       break
    else:
         username = username + "\n" 
         with open(filename, 'a') as file_object:
          file_object.write(username)
    print 'The Progrommer is over! your input name is %s' %username 
get_input()
#import json
#numbers = [2,3,5,7,11,13]
#filename = 'numbers.json'
#with open (filename,'w') as file_object:
# json.dump(numbers,file_object)
