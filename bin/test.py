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
# import re
# def get_ini():
#     with open('setting.ini','r',errors='ignore') as f:
#         data=f.readlines()
#     return [data[4].replace('\n',''),data[5].replace('\n','')]
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
# import cx_Oracle
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

# from cqs_pt_rating_database import get_ini
# db_connect=get_ini()[0]
# def get_connectionid():
#     conn = cx_Oracle.connect(db_connect)
#     cur =conn.cursor()
#     r= cur.execute("select max(connection_id) from CUX.CUX_CQS_BRANCH_CONNECT_HIS_T")
#     conn_id=[]
#     for row in cur:
#         conn_id.extend(row)
#     print('数据库中最大的Conn_ID为')
#     print(max(conn_id))
#     return max(conn_id)
#
# print(get_connectionid())

# from check_legal import check_batch_id
# flag=check_batch_id()[0]
# print(flag)
# a=[1,1,2,3,3]
# print(min(a))
# from cqs_branch_connect_database import *
# from check_legal import *
# flag=check_batch_id()[0]
# print(flag)
# if flag is False:
#     print('本次导入失败，部分等级表无法被写入数据库，将执行删除操作')
#     min_batch_id=min(check_batch_id()[1])
#     sql_commands=make_sql_str(min_batch_id)
#     print(sql_commands)
#     s=list(map(del_rest_data,sql_commands))
#     print('删除成功')
# else:
#     print('success')

# def check_continue():
#     while True:
#         try:
#             check_flag=int(input('\n请输入一个数字，0表示正常类型，1表示续传类型：'))
#             if -1<check_flag<2:
#                 break
#             else:
#                 print('尽可以允许输入0和1')
#         except ValueError:
#             print("Oops!  That was no valid number.  Try again...")
#     return check_flag
# s=check_continue()
# print(s)
# print(1%2)

# import time
# today_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
# today_time=today_time.replace('-','/')
# print(today_time)
# import cx_Oracle
# from cqs_pt_rating_database import get_ini
# db_connect=get_ini()[0]
# def is_number(s):
#     try:
#         float(s)
#         return True
#     except ValueError:
#         pass
#
#     try:
#         import unicodedata
#         unicodedata.numeric(s)
#         return True
#     except (TypeError, ValueError):
#         pass
#
#     return False
# print(is_number('123'))
# def return_domain_username():
#     username=101087
#     sql="select fu.user_id from fnd_user fu where fu.user_name ='%s'"%username
#     conn = cx_Oracle.connect(db_connect)
#     cur =conn.cursor()
#     cur.execute(sql)
#     result=cur.fetchone()
#     return result
#
# print(return_domain_username()[0])
# username=100232
# sql="select fu.description from fnd_user fu where fu.user_name ='%s'"%username
# conn = cx_Oracle.connect(db_connect)
# cur =conn.cursor()
# cur.execute(sql)
# result=cur.fetchone()
# print(result[0])

# def return_formal_creater(change_batch_id):
#     conn = cx_Oracle.connect(db_connect)
#     cur =conn.cursor()
#     sql='select created_by from CUX.CUX_CQS_BRANCH_CONNECT_HIS_T where batch_id=%s'%change_batch_id
#     r= cur.execute(sql)
#     result=cur.fetchone()
#     new_result=list(result)
#     return new_result[0]
#
# print(return_formal_creater(14))
#
# import winreg
# key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,r"Software\Microsoft\Windows\CurrentVersion\Explorer")
# try:
#     i=0
#     while 1:
#         name, value, type = winreg.EnumValue(key, i)
#         print(repr(name),repr(value),repr(type))
#         i+=1
# except WindowsError:
#     print('finish')
# from cqs_pt_rating_database import get_ini
# db_connect=get_ini()[0]
# import cx_Oracle
# conn = cx_Oracle.connect(db_connect)
# cur =conn.cursor()
# r= cur.execute("select max(batch_id) from CUX.CUX_CQS_BRANCH_CONNECT_T")
# result=cur.fetchone()
# new_result=list(result)
# print(type(new_result[0]))
# import cx_Oracle
# from cqs_pt_rating_database import get_ini
# db_connect=get_ini()[0]
# conn = cx_Oracle.connect(db_connect)
# cur =conn.cursor()
# r= cur.execute("select max(batch_id) from CUX.CUX_CQS_BRANCH_CONNECT_T")
# result=cur.fetchone()
# new_result=list(result)
# f=open("change_valid_id.txt",'w')
# f.write(str(new_result[0]))
#
# f=open('change_valid_id.txt','r')
# data=f.readline()
# print(int(data))

# from ftplib import FTP
# import os,time,shutil,re
# from cqs_branch_connect_database import get_batch_id
# import socket
#
# def get_ini():
#     with open('setting.ini','r',errors='ignore') as f:
#         data=f.readlines()
#     return [data[4].replace('\n',''),data[5].replace('\n','')]
# db_connect=get_ini()[1]
# def get_path():
#     import os
#     current_path=os.path.abspath(os.path.join(os.path.dirname('cqs_index.py'),os.path.pardir))
#     new_path=current_path+'\\'+'excel\\'
#     FileList = []
#     rootdir = new_path
#     for root, subFolders, files in os.walk(rootdir):
#         #排除特定的子目录
#         if 'done' in subFolders:
#             subFolders.remove('done')
#         #查找特定扩展名的文件，只要包含'索引表'但不包含"new"字符串的文件，都会被包含
#         for f in files:
#             if f.find('表') != -1 and f.find('new')==-1:
#                 FileList.append(os.path.join(root, f))
#     return FileList
#
#
# if __name__ == '__main__':
#     ftp_ini=get_ini()[1]
#     today_time=time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
#     new_ftp_path=str(today_time)+' '+str(get_batch_id())
#     parent_path=os.path.abspath(os.path.join(os.path.dirname('cqs_index.py'),os.path.pardir))
#     os.chdir(parent_path)
#     remotepath='/'+new_ftp_path+'/'
#     # file_path='/backup/'+new_ftp_path
#     os.mkdir(new_ftp_path)
#     base_path=os.getcwd()#获取当前目录
#     namelist=get_path()
#     for name in namelist:
#         shutil.copy(name,new_ftp_path)
#         print(name)
#     excel_path=base_path+'\\'+new_ftp_path
#     os.chdir(excel_path)
#     print(os.getcwd())
#     namelist=get_path()
#     count_index=1
#     count_rate=1
#     ftp_name=re.findall('(.*?)/',ftp_ini)
#     ftp_pass=re.findall('/(.*?)@',ftp_ini)
#     ftp_ip=re.findall('@(.*?):',ftp_ini)
#     row_ftp_port=re.findall(':\d*',ftp_ini)
#     ftp_port=row_ftp_port[0].replace(':','')
#     ftp=FTP()
#     try:
#         ftp.connect(host='192.168.15.85',port='21')
#     except (socket.error, socket.gaierror):
#         print('ERROR:cannot reach " %s"' % ftp_ip)
#     print('***Connected to host "%s"' % ftp_ip)
#     ftp.login(user=ftp_name,passwd=ftp_pass)
#     print(ftp.dir())
# import time
# fmt = '{:3d} [{:<20}]'.format
# def progressbar():
#     for n in range(21):
#         time.sleep(0.1)
#         print('\r',fmt(n*5, '='*n),)
#
# progressbar()
# import time
# from progressbar import AnimatedMarker, Bar, BouncingBar, Counter, ETA, \
#     AdaptiveETA, FileTransferSpeed, FormatLabel, Percentage, \
#     ProgressBar, ReverseBar, RotatingMarker, \
#     SimpleProgress, Timer
#
#
# pbar = ProgressBar(maxval=100).start()
# pbar.update(10)
# time.sleep(2)
# pbar.update(50)
# time.sleep(3)
# pbar.update(100)
# pbar.finish()
from colorama import init, Fore, Back, Style
if __name__ == "__main__":

    init(autoreset=True)    #  初始化，并且设置颜色设置自动恢复
    print(Fore.RED + 'some red text')
    print(Back.GREEN + 'and with a green background')
    print(Style.DIM + 'and in dim text')
    # 如果未设置autoreset=True，需要使用如下代码重置终端颜色为初始设置
    #print(Fore.RESET + Back.RESET + Style.RESET_ALL)  autoreset=True
    print('back to normal now')
