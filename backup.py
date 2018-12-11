#!/usr/bin/python
# - * - coding: utf-8 - * -
#将source目录全部整合打包到target_dir
import os
import time
# 1. 备份源目录
source = ['/home/swaroop/byte', '/home/swaroop/bin']
# If you are using Windows, use source = [r'C:\Documents', r'D:\Work'] or something like that
# 2. 备份目的目录
target_dir = '/mnt/e/backup/' 
# 3. 遍历source，判断目录是否存在，不存在全部创建
for yuansu in source:
 if not os.path.isdir(yuansu):
  os.makedirs(yuansu)
  print 'local path already created' ,  yuansu
# 4. 定义时间戳
today = target_dir + time.strftime('%Y%m%d')
# The current time is the name of the zip archive
now = time.strftime('%H%M%S')
## Take a comment from the user to create the name of the zip file
# 5. 交互式定义最终备份文件名
comment = raw_input('Enter a comment: ')
if len(comment) == 0: # check if a comment was entered
 target = today + os.sep + now + '.zip'
else:
 target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.zip'
## Notice the backslash!
## Create the subdirectory if it isn't already there
# 6. 判断today目录是否存在，不存在创建，并输出Successfully
if not os.path.isdir(today):
 os.makedirs(today) # make directory
 print 'Successfully created directory' , today
#
## 7. 执行linux备份命令，获取返回值，成功则输出Successful，不成功则输出Backup FAILED
zip_command = "zip -qr '%s' %s" % (target, ' '.join(source)) 
if os.system(zip_command) == 0:
 print 'Successful backup to', target 
else:
 print 'Backup FAILED'
#
