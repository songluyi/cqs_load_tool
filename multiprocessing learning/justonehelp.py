# -*- coding: utf-8 -*-
import os
import sys
import codecs
import urllib,requests
result=requests.get('http://news.gtimg.cn/more.php?q=usJD&page=1')
# data=result.text.replace('var finance_news =','')
# data=eval(data.replace(';',''))
# print(data['data'][2][2])
# print(data)
data=result.text
# print(data)
data1=data.encode('ISO8859-1','ignore')
print(data1.decode('gbk'),'ignore')

# print(data.decode('gbk'))
# print(data.decode('utf-8'))