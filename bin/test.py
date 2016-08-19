# -*- coding: utf-8 -*-
# 2016/8/5 9:05
"""
-------------------------------------------------------------------------------
Function:
Version:    1.0
Author:     SLY
Contact:    slysly759@gmail.com 
 
-------------------------------------------------------------------------------
"""
# for i in range(1,100):
#     i=str(i)
#     url='https://xueqiu.com/stock/cata/stocklist.json?page='+i+'&size=30&order=desc&orderby=percent&exchange=CN&plate=A%%E8%%82%%A1%%E6%%8C%%87%%E6%%95%%B0&_=1470367605448'
#     print(url)

# a='12锅炉范围内管道应采用GB 3087标准。'
# if ord(a[1])>60:
#     NOTE_KEY='注'+str(a[0])
#     print(NOTE_KEY)
# else:
#     NOTE_KEY='注'+str(a[0])+str(a[1])
#     print(NOTE_KEY)
# for i in range(345,500):
#     print(i)
# import cx_Oracle
# print('ok')
import re
def get_ini():
    with open('setting.ini','r',errors='ignore') as f:
        data=f.readlines()
    return [data[4].replace('\n',''),data[5].replace('\n','')]
# str='admin/admin@127.0.0.1:22'
# result=re.findall('(.*?)/',str)
# print(result[0])
# ftp_ini=get_ini()[1]
# ftp_name=re.findall('(.*?)/',ftp_ini)
# ftp_pass=re.findall('/(.*?)@',ftp_ini)
# ftp_ip=re.findall('@(.*?):',ftp_ini)
# row_ftp_port=re.findall(':\d*',ftp_ini)
# ftp_port=row_ftp_port[0].replace(':','')
# ftp=paramiko.Transport((ftp_ip, int(ftp_port)))
import cx_Oracle
# from cqs_pt_rating_database import get_ini
# db_connect=get_ini()[0]
# def get_batch_id():
#     conn = cx_Oracle.connect(db_connect)
#     cur =conn.cursor()
#     r= cur.execute("select max(batch_id) from CUX.CUX_CQS_BRANCH_CONNECT_HIS_T")
#     result=cur.fetchone()
#     new_result=list(result)
#     return new_result[0]
#
# a=get_batch_id()
# print(a)

from cqs_pt_rating_database import get_ini
db_connect=get_ini()[0]
def get_connectionid():
    conn = cx_Oracle.connect(db_connect)
    cur =conn.cursor()
    r= cur.execute("select max(connection_id) from CUX.CUX_CQS_BRANCH_CONNECT_HIS_T")
    conn_id=[]
    for row in cur:
        conn_id.extend(row)
    print('数据库中最大的Conn_ID为')
    print(max(conn_id))
    return max(conn_id)

print(get_connectionid())