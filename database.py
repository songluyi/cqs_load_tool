# -*- coding: utf-8 -*-
# 2016/7/15 13:36
"""
-------------------------------------------------------------------------------
Function:
Version:    1.0
Author:     SLY
Contact:    slysly759@gmail.com 
 
-------------------------------------------------------------------------------
"""
# import os
# import cx_Oracle
# from openpyxl import Workbook
# from openpyxl import load_workbook
#
# load_name=r'test.xlsx'
# wb_load = load_workbook(filename=load_name)
# sheets = wb_load.get_sheet_names()
# data=[]
# ws_load = wb_load.get_sheet_by_name(sheets[0])
# for i in range(1,42):
#     once_data=ws_load.cell(row=1, column=i).value
#     data.append(once_data)
#
# print(data)
# from openpyxl import Workbook
# from openpyxl import load_workbook
# header_name=['INDEX_ID', 'INDEX_ORDER', 'CATAGORY', 'SERVICES', 'DESIGN_TEMP_SOURCE', 'DESIGN_TEMP_MIN',
#              'DESIGN_TEMP_MAX', 'DESIGN_TEMP_SPEC', 'DESIGN_PRES_SOURCE', 'DESIGN_PRES_MIN',
#              'DESIGN_PRES_MAX', 'DESIGN_PRES_SPEC', 'PIPING_MATL_CLASS', 'BASIC_MATERIAL', 'RATING',
#              'FLANGE_FACING', 'CA', 'NOTE', 'BATCH_ID', 'CREATED_BY', 'CREATION_DATE', 'LAST_UPDATED_BY',
#              'LAST_UPDATE_DATE', 'LAST_UPDATE_LOGIN', 'ATTRIBUTE_CATEGORY', 'ATTRIBUTE1', 'ATTRIBUTE2',
#              'ATTRIBUTE3', 'ATTRIBUTE4', 'ATTRIBUTE5', 'ATTRIBUTE6', 'ATTRIBUTE7', 'ATTRIBUTE8', 'ATTRIBUTE9',
#              'ATTRIBUTE10', 'ATTRIBUTE11', 'ATTRIBUTE12', 'ATTRIBUTE13', 'ATTRIBUTE14', 'ATTRIBUTE15', 'ROWID']
# load_name='test.xlsx'
# wb_load = load_workbook(filename=load_name)
# sheets = wb_load.get_sheet_names()
# ws_load = wb_load.get_sheet_by_name(sheets[0])
#
# wb_write=Workbook()
# ws_write = wb_write.get_active_sheet()
# ws_write.title = 'PMC Index (Sorted by Services)'
# #写入基本的excel表头
# for i in range(1,41):
#     ws_write.cell(row=1, column=i).value = header_name[i]
# wb_write.save(filename='new_file.xlsx')
#
# import time
# today_time=time.strftime("%Y-%m-%d", time.localtime())
# today_time=today_time.replace('-','/')
# print(today_time)
#
# a='1.烟尘类'
# b='119'
# print(len(b))
# print(len(a))
# a=0
# if a<5:
#     print(a)
# elif a<3:
#     print(a)
#     print('aaa')
# import os
# path=os.getcwd()
# FileList = []
# rootdir = path
#
# for root, subFolders, files in os.walk(rootdir):
#     #排除特定的子目录
#     if 'done' in subFolders:
#         subFolders.remove('done')
#     #查找特定扩展名的文件，只要包含'.py'字符串的文件，都会被包含
#     for f in files:
#         if f.find('.xlsx') != -1:
#             FileList.append(os.path.join(root, f))
#
# for item in FileList:
#     print(item)
#     print(os.path.basename(item))


import cx_Oracle
def get_indexid():
    conn = cx_Oracle.connect("apps/apps@192.168.15.94:1539/NRCRP2")
    cur =conn.cursor()
    r= cur.execute("select t.index_id from CUX.CUX_CQS_INDEX_T t")
    index_id=[]
    for row in cur:
        index_id.extend(row)
    print('数据库中最大的Index_ID为')
    print(max(index_id))
    return max(index_id)

def insert_db(self,header_name):
    conn = cx_Oracle.connect("apps/apps@192.168.15.94:1539/NRCRP2")
    cur =conn.cursor()
    db_name='CUX.CUX_CQS_INDEX_T'

    r= cur.execute("select t.index_id from CUX.CUX_CQS_INDEX_T t")
