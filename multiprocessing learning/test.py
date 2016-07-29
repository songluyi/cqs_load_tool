# -*- coding: utf-8 -*-
# 2016/7/25 8:59
"""
-------------------------------------------------------------------------------
Function:
Version:    1.0
Author:     SLY
Contact:    slysly759@gmail.com 
 
-------------------------------------------------------------------------------
"""
import cx_Oracle
# count=1
# print('number=%d')

# if pres_data=="常压":
#     ws_write.cell(row=line+space_tab, column=10).value=0
#     ws_write.cell(row=line+space_tab, column=11).value=1
#     ws_write.cell(row=line+space_tab, column=12).value=pres_data
# line=1
# print('已经插入数据，行数为',line,'hello')
# import multiprocessing
# print(multiprocessing.cpu_count())
# n = 16
# myDict = {}
# for i in range(0, n):
#     char = 'abcd'[i%4]
#     try:
#         myDict[char] += 1
#     except KeyError:
#         myDict[char] = 1
#     print(myDict)

'''''
Created on 2016年7月7日
@author: Tommy
'''
# import cx_Oracle
#
# class Oracle(object):
#     """  oracle db operator  """
#     def __init__(self,userName,password,host,instance):
#         self._conn = cx_Oracle.connect("%s/%s@%s/%s" % (userName,password,host,instance))
#         self.cursor = self._conn.cursor()
#
#     def queryTitle(self,sql,nameParams={}):
#         if len(nameParams) > 0 :
#             self.cursor.execute(sql,nameParams)
#         else:
#             self.cursor.execute(sql)
#
#         colNames = []
#         for i in range(0,len(self.cursor.description)):
#             colNames.append(self.cursor.description[i][0])
#
#         return colNames
#
#     # query methods
#     def queryAll(self,sql):
#         self.cursor.execute(sql)
#         return self.cursor.fetchall()
#
#     def queryOne(self,sql):
#         self.cursor.execute(sql)
#         return self.cursor.fetchone()
#
#     def queryBy(self,sql,nameParams={}):
#         if len(nameParams) > 0 :
#             self.cursor.execute(sql,nameParams)
#         else:
#             self.cursor.execute(sql)
#
#         return self.cursor.fetchall()
#
#     def insertBatch(self,sql,nameParams=[]):
#         """batch insert much rows one time,use location parameter"""
#         self.cursor.prepare(sql)
#         self.cursor.executemany(None, nameParams)
#         self.commit()
#
#     def commit(self):
#         self._conn.commit()
#
#     def __del__(self):
#         if hasattr(self,'cursor'):
#             self.cursor.close()
#
#         if hasattr(self,'_conn'):
#             self._conn.close()
#
#
#
#
#
# def test1():
#     # sql = """select user_name,user_real_name,to_char(create_date,'yyyy-mm-dd') create_date from sys_user where id = '10000' """
#     sql = """select user_name,user_real_name,to_char(create_date,'yyyy-mm-dd') create_date from sys_user where id =: id """
#     oraDb = Oracle('test','java','192.168.0.192','orcl')
#
#     fields = oraDb.queryTitle(sql, {'id':'10000'})
#     print(fields)
#
#     print(oraDb.queryBy(sql, {'id':'10000'}))
#
# def test2():
#     oraDb = Oracle('test','java','192.168.0.192','orcl')
#     cursor = oraDb.cursor
#
#     create_table = """
#     CREATE TABLE python_modules (
#     module_name VARCHAR2(50) NOT NULL,
#     file_path VARCHAR2(300) NOT NULL
#     )
#     """
#     from sys import modules
#
#     cursor.execute(create_table)
#     M = []
#     for m_name, m_info in modules.items():
#         try:
#             M.append((m_name, m_info.__file__))
#         except AttributeError:
#             pass
#
#     sql = "INSERT INTO python_modules(module_name, file_path) VALUES (:1, :2)"
#     oraDb.insertBatch(sql,M)
#
#     cursor.execute("SELECT COUNT(*) FROM python_modules")
#     print(cursor.fetchone())
#     print('insert batch ok.')
#
#     cursor.execute("DROP TABLE python_modules PURGE")
#
# test2()

# a='b1b8b0c6ad85528e144a433c6882f93e'
# print(len(a))
import cx_Oracle
# conn = cx_Oracle.connect("apps/apps@192.168.15.94:1539/NRCRP2")
# cur =conn.cursor()
# r= cur.execute("select max(batch_id) from CUX.CUX_CQS_INDEX_HIS_T")
# # batch_id=[]
# # for row in cur:
# #         batch_id.extend(row)
# # print(batch_id)
# # print(max(batch_id))
# result=cur.fetchone()
# new_result=list(result)
# print(new_result)
# print(new_result[0])
# conn = cx_Oracle.connect("apps/apps@192.168.15.94:1539/NRCRP2")
# cur =conn.cursor()
# r= cur.execute("select max(batch_id) from CUX.CUX_CQS_BRANCH_CONNECT_HIS_T")
# result=cur.fetchone()
# new_result=list(result)
# print(new_result[0])
#
# from openpyxl import Workbook
# from openpyxl import load_workbook
# load_name="1.xlsx"
# wb_load = load_workbook(filename=load_name)
# sheets = wb_load.get_sheet_names()
# ws_load=wb_load.get_sheet_by_name(sheets[0])
# data=[]
# for i in range(1,24):
#     data.append(ws_load.cell(row=1, column=i).value)
#
# print(data)


# a='2.对焊端部厚度与相连管道的壁厚相同。'
# print(a[0])

# header_name=['NOTE_ID', 'SERVICE_SOURCE', 'NOTE_KEY', 'NOTE', 'BATCH_ID', 'CREATED_BY', 'CREATION_DATE',
#              'LAST_UPDATED_BY', 'LAST_UPDATE_DATE', 'LAST_UPDATE_LOGIN', 'ATTRIBUTE_CATEGORY',
#              'ATTRIBUTE1', 'ATTRIBUTE2', 'ATTRIBUTE3', 'ATTRIBUTE4', 'ATTRIBUTE5', 'ATTRIBUTE6',
#              'ATTRIBUTE7', 'ATTRIBUTE8', 'ATTRIBUTE9', 'ATTRIBUTE10', 'ATTRIBUTE11', 'ATTRIBUTE12',
#              'ATTRIBUTE13', 'ATTRIBUTE14', 'ATTRIBUTE15']
# data=[]
# for i in header_name:
#     i=':'+i+','
#     data.append(i)
# a=''.join(data)
# print(a)
# today_time='2016/7/29'
# creation_date=last_update_date=today_time
# print(creation_date,last_update_date)
# header_name=['BATCH_ID', 'COMMENTS', 'CREATION_DATE', 'LAST_UPDATE_DATE', 'CREATED_BY',
#              'LAST_UPDATED_BY', 'LAST_UPDATE_LOGIN', 'ATTRIBUTE_CATEGORY', 'ATTRIBUTE1', 'ATTRIBUTE2',
#              'ATTRIBUTE3', 'ATTRIBUTE4', 'ATTRIBUTE5', 'ATTRIBUTE6', 'ATTRIBUTE7', 'ATTRIBUTE8',
#              'ATTRIBUTE9', 'ATTRIBUTE10', 'ATTRIBUTE11', 'ATTRIBUTE12', 'ATTRIBUTE13',
#              'ATTRIBUTE14', 'ATTRIBUTE15']
# comments=input('请输入一段描述方便自己日后恢复数据:')
# batch_id=1
# creation_date=last_update_date='2016/7/29'
# data=[]
# created_by=last_update_by=0
# last_update_login=1
# data.append(batch_id);data.append(comments);data.append(creation_date);data.append(last_update_date)
# data.append(created_by);data.append(last_update_by);data.append(last_update_login)#目前没想到追加的好方式，打算自己造一个轮子批量append
# print(data)
# row=dict(zip(header_name,data))
# print(row)
# print(len(row))
# row=[]
# for i in header_name:
#     i=':'+i+','
#     row.append(i)
# a=''.join(row)
# print(a)

b={ 'BATCH_ID':1, 'COMMENTS': 'test','CREATION_DATE': '2016/7/29','LAST_UPDATE_DATE': '2016/7/29','CREATED_BY':0, 'LAST_UPDATED_BY':1,'LAST_UPDATE_LOGIN':1,}
print(len(b))
print(b)
conn = cx_Oracle.connect("apps/apps@192.168.15.94:1539/NRCRP2")
cur =conn.cursor()
r=cur.execute(" insert into cux.cux_cqs_batchs_t(BATCH_ID,COMMENTS,CREATION_DATE,LAST_UPDATE_DATE,CREATED_BY,LAST_UPDATED_BY,LAST_UPDATE_LOGIN) values (:BATCH_ID,:COMMENTS,to_date(:CREATION_DATE,'yyyy/mm/dd'),to_date(:LAST_UPDATE_DATE,'yyyy/mm/dd'),:CREATED_BY,:LAST_UPDATED_BY,:LAST_UPDATE_LOGIN)", b)
conn.commit()
print('数据已经导入成功')
#
# header_name=['BATCH_ID', 'COMMENTS', 'CREATION_DATE', 'LAST_UPDATE_DATE', 'CREATED_BY',
#              'LAST_UPDATED_BY', 'LAST_UPDATE_LOGIN', 'ATTRIBUTE_CATEGORY', 'ATTRIBUTE1', 'ATTRIBUTE2',
#              'ATTRIBUTE3', 'ATTRIBUTE4', 'ATTRIBUTE5', 'ATTRIBUTE6', 'ATTRIBUTE7', 'ATTRIBUTE8',
#              'ATTRIBUTE9', 'ATTRIBUTE10', 'ATTRIBUTE11', 'ATTRIBUTE12', 'ATTRIBUTE13',
#              'ATTRIBUTE14', 'ATTRIBUTE15']
# a=[]
# for i in header_name:
#     i=i+','
#     a.append(i)
# print(''.join(a))
