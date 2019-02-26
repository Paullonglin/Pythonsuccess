# coding=utf-8
import requests
from bs4 import BeautifulSoup
import re
url='https://www.biqukan.com/12_12479/'
nurl='https://www.biqukan.com'
try:
    r = requests.get(url)
    r.raise_for_status()
    demo = r.text
except:
    print('爬取失败')

soup = BeautifulSoup(demo, 'html.parser')
tit=soup.dt.text
newtit=tit[0:11]
fo=open(r'D:\PXiaoshuo\屌丝道士\{}.txt'.format(newtit),'w',encoding='utf-8')
for link in soup.find_all(href=re.compile("/12_12479/")):
    fo.writelines(nurl+link.get('href')+' '+link.string+'\n')
print('爬取完成')
fo.close()
