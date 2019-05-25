#!/usr/bin/python
# -*- coding: UTF-8 -*-
```找出列表中的最大值，并且与列表的最后一个值互换位置```
list1 = [5, 12, 32, 4, 2, 10, 25]
count = 0
for i in list1:
    count += 1
    n = len(list1)
    if i == max(list1):
            #a = list1[count-1]
            #b = list1[n-1]
            #list1[count-1] = b
            #list1[n-1] = a
        list1[count-1],list1[n-1] = list1[n-1],list1[count-1]
print(list1)


输出结果:
[5, 12, 25, 4, 2, 10, 32]
