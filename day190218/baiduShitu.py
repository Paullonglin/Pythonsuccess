from aip import AipOcr
import re

""" 你的 APPID AK SK """
APP_ID = '15581478'
API_KEY = '2srxZo33pGbDHLLCy27tBPux'
SECRET_KEY = '1OLDAfzSVxlSYnyKSvFq8ncWvWgXwvt5'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

i=open(r'D:\TP\2.png','rb')
img=i.read()
message=client.basicGeneral(img)
# of=open(r'D:\TP\1.txt','a+',encoding='utf-8')
for i in message.get('words_result'):

#     of.writeline(i.get('words'))
# print('写入成功')
    print(i.get('words'))
