#!/usr/bin/python
# - * - coding: utf-8 - * -
#计算十二生肖
#raw_input出来的都是字符串，所以要加int转换为整数类型
#shengxiao被定义为列表
shengxiao = [ '猴','鸡','狗','猪','鼠','牛','虎','兔','龙','蛇','马','羊']
wangwangjie = int(raw_input("请输入您的出生日期，方便计算您的生肖:"))
print "您的生肖是" , shengxiao[ wangwangjie % 12 ]
