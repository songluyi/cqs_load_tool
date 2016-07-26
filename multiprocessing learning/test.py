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

