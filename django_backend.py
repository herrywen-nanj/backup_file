import urllib.request
import re

#page = urllib.request.urlopen('http://192.168.5.148:60001/')
#html = page.read().decode('utf-8')
# Python3 findall数据类型用bytes类型
# or html=urllib.urlopen(url).read()

#title=re.findall('<title>(.+)</title>',html)
#print (title)

def detect_website():
     filename = "url.txt"
     with open(filename)  as  file_object:
          lines = file_object.read().splitlines()
     for url in lines:
          page = urllib.request.urlopen(url)
          html = page.read().decode('utf-8')
          title=re.findall('<title>欢迎使用云平台(.+)服务</title>',html)
          if title == None:
             print("title  没有找到")
          else:
             service_name_version = " ".join(title)
             a = service_name_version.split(' ')
             content = "服务url是" + url + "," + "服务名称是:"  + a[0] + "," + "版本号是:" + a[1]
             print(content)
    






detect_website()
