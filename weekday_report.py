#!/usr/bin/python
# - * - coding: utf-8 - * -
#作用：写周报
import datetime
filename = '1.txt'
string_date = '%Y年-%m月-%d日'
weekdate = []
raw_content = []
def getYesterday(): 
   #获取一周每天的时间戳且格式化
    today=datetime.date.today()
    for i in range(0,5):
     oneday=datetime.timedelta(days=i)
     yesterday=today-oneday
     yesterday = yesterday.strftime(string_date)  
     weekdate.append(yesterday)

getYesterday()
weekdate.reverse()


def get_rawcontent():
   #获取周报内容
 j = 0
 while j< 5:
  content = raw_input("please input you content: ")
  raw_content.append(content)
  j += 1
get_rawcontent()

def get_report():
 #整合内容
 for i in range(0,5):
   count_report = weekdate[i] + ' ' + raw_content[i] + "\n"
   with open(filename,'a') as file_object:
     file_object.write(count_report)
get_report()


 1.安装yum install -y  virt-*  libvirt  bridge-utils qemu-img
 2.mkdir /kvm_data && mkfs.xfs /dev/sdb && mount /dev/sdb /kvm_data
 3.systemctl start  libvirtd
4.安装kvm:virt-install --name=aminglinux01 --memory=512,maxmemory=1024 --vcpus=1,maxvcpus=2 --os-type=linux --os-variant=rhel7 --location=/kvm_data/CentOS-7-x86_64-DVD-1804.iso --disk path=/kvm_data/aminglinux01.img,size=10 --bridge=br0 --graphics=none --console=pty,target_type=serial  --extra-args="console=tty0 console=ttyS0"
5.pip install numpy -i http://pypi.douban.com/simple --trusted-host pypi.douban.com





