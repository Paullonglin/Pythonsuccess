# coding=utf-8
import requests
from bs4 import BeautifulSoup
import re
foo=open(r'D:\PXiaoshuo\屌丝道士\《屌丝道士之厄运起源》.txt','r',encoding='utf-8')
read=foo.readline()
newread=read.split(' ')
newurl=newread[0]
title=newread[1:3]
t2=title[0]+title[1]
titleread=t2.split('\n')
newtitle=titleread[0]
print(newurl)
print(newtitle)
foo.close()

try:
    r = requests.get(newurl)
    r.encoding=r.apparent_encoding
    r.raise_for_status()
    demo = r.text
except:
    print('爬取失败')
# soup = BeautifulSoup(demo, 'html.parser')
# test=soup.find(id="content")
# fo=open(r'D:\PXiaoshuo\屌丝道士\{}.txt'.format(newtitle),'w',encoding='utf-8')
# fo.writelines(test.text)
# print('爬取完成')
# fo.close()
# fo=open(r'D:\PXiaoshuo\屌丝道士\{}.txt'.format(newtitle),'r',encoding='utf-8')
# read=fo.readlines()
# print('读取完成')
# fo.close()
# sep='\n'
# fo=open(r'D:\PXiaoshuo\屌丝道士\{}.txt'.format(newtitle),'w',encoding='utf-8')
# wt=fo.writelines(sep.join(read))
# print('写入完成')
# fo.close()

