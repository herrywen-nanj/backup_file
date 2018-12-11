#!/usr/bin/python
# - * - coding: utf-8 - * -
#检测程序端口是否开启，告诉你哪些端口可以使用
import os
def detectPort():
 a = [80,90,91]
 c = []
#print 'a数组是' , a
 for port in a:
     command = "lsof -i:{}".format(port)
    #print '你的端口分别是' , command
     if os.system(command) != 0:
        c.append(port)
 print '您可用的端口还有' + ','.join(str(i) for i in c)
detectPort()
