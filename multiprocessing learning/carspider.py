# -*- coding: utf-8 -*-
# 2016/7/30 21:39
"""
-------------------------------------------------------------------------------
Function:   crawl some car information
Version:    1.0
Author:     SLY
Contact:    slysly759@gmail.com 
 
-------------------------------------------------------------------------------
"""

import requests,time

for i in range(1,71):
    base_url='http://select.car.yiche.com/selectcartool/searchresult?page='+str(i)+'&external=Car&callback=jsonpCallback'
    query=requests.get(base_url)
    time.sleep(1)
    row_data=query.content
    row_data=row_data.decode('utf-8')
    data=row_data.replace('jsonpCallback','')
    data=str(data.replace('(',''))
    data=str(data.replace(')',''))
    data=str(data.replace("b'",''))
    data=str(data.replace("'",''))
    # print(data)
    new_data=eval(data)
    # print(len(new_data['ResList']))
    for i in range(0,20):
        print(new_data['ResList'][i]['ShowName'],':',new_data['ResList'][i]['PriceRange'])