# coding=utf-8
import requests
from bs4 import BeautifulSoup
import re
# fo=open(r'D:\PXiaoshuo\屌丝道士\《屌丝道士之厄运起源》.txt','r',encoding='utf-8')
# read=fo.readline()
# newread=read.split(' ')
# newurl=newread[0]
# newtitle=newread[-1]
# print(newurl)
# print(newtitle)
# fo.close()
url='https://www.biqukan.com/12_12479/23430723.html'
try:
    r = requests.get(url)
    r.encoding=r.apparent_encoding
    r.raise_for_status()
    demo = r.text
except:
    print('爬取失败')
soup = BeautifulSoup(demo, 'html.parser')
test=soup.find(id="content")
fo=open(r'D:\PXiaoshuo\屌丝道士\{}.txt'.format('第六百四十三节 食尸鼠'),'w',encoding='utf-8')
fo.writelines(test.text)
print('爬取完成')
fo.close()
fo=open(r'D:\PXiaoshuo\屌丝道士\{}.txt'.format('第六百四十三节 食尸鼠'),'r',encoding='utf-8')
read=fo.readlines()
print('读取完成')
fo.close()
sep='\n'
fo=open(r'D:\PXiaoshuo\屌丝道士\{}.txt'.format('第六百四十三节 食尸鼠'),'w',encoding='utf-8')
wt=fo.writelines(sep.join(read))
print('写入完成')
fo.close()

