# -*- coding: utf-8 -*-
# 2016/7/18 9:18
"""
-------------------------------------------------------------------------------
Function:
Version:    1.0
Author:     SLY
Contact:    slysly759@gmail.com 
 
-------------------------------------------------------------------------------
"""
# from openpyxl import load_workbook
# name='branch_connect.xlsx'
# wb_load = load_workbook(filename=name)
# sheets = wb_load.get_sheet_names()
# ws_load = wb_load.get_sheet_by_name(sheets[0])
# data=[]
# for i in range(1,29):
#     data.append(ws_load.cell(row=1, column=i).value)
# print(data)

# for i in range(13,500):
#     if '备注' in str(ws_load.cell(row=i, column=1).value):
#         od=i-1#向上提一行
# for i in range(13,od):
#     if ws_load.cell(row=i, column=1).value is not None and ws_load.cell(row=i, column=4).value is None:
#         data.append(i)
# data.append(od)
# print(data)
# print(data)

# import os
# path=os.getcwd()
# FileList = []
# rootdir = path
#
# for root, subFolders, files in os.walk(rootdir):
#     #排除特定的子目录
#     if 'done' in subFolders:
#         subFolders.remove('done')
#     #查找特定扩展名的文件，只要包含'索引表'但不包含"new"字符串的文件，都会被包含
#     for f in files:
#         if f.find('等级表') != -1 and f.find('new')==-1:
#             FileList.append(os.path.join(root, f))
#
# for item in FileList:
#     print('检测到您目录下有如下excel文件 请确保他们是要提交的管道等级索引表')
#     print(item)
# from openpyxl import load_workbook
# load_name='管道材料等级表.xlsx'
# wb_load = load_workbook(filename=load_name)
# sheets = wb_load.get_sheet_names()
# del sheets[-1]
# for page_name in sheets[::2]:#循环页签
# ws_load = wb_load.get_sheet_by_name(page_name)
# header_name=['CONNECTION_ID', 'BATCH_ID', 'CONN_ORDER_NUMBER', 'PIPING_MATL_CLASS', 'BRANCH_DN',
#              'HEADER_DN', 'CONNECTION_TYPE', 'CREATED_BY', 'CREATION_DATE', 'LAST_UPDATED_BY',
#              'LAST_UPDATE_DATE', 'LAST_UPDATE_LOGIN', 'ATTRIBUTE_CATEGORY', 'ATTRIBUTE1', 'ATTRIBUTE2',
#              'ATTRIBUTE3', 'ATTRIBUTE4', 'ATTRIBUTE5', 'ATTRIBUTE6', 'ATTRIBUTE7', 'ATTRIBUTE8',
#              'ATTRIBUTE9', 'ATTRIBUTE10', 'ATTRIBUTE11', 'ATTRIBUTE12', 'ATTRIBUTE13', 'ATTRIBUTE14',
#              'ATTRIBUTE15']
# new_list=[]
# for name in header_name:
#     name=':'+name+','
#     new_list.append(name)
# print(new_list)
# b=''.join(new_list)
# print(b)
# a=[]
# print(len(a))
# for i in range(13,16):
#     print(i)

# i=[1,2,3,4,5,6,7]
# a=i[1::2]
# print(a)
# print([x for x in range(4,35)][::2])

# import time,re
# import os,datetime
# from concurrent import futures
# def wait_on_b():
#     print(5)
#     time.sleep(2)
# def wait_on_a():
#     print(6)
#     time.sleep(2)
# ex = futures.ThreadPoolExecutor(max_workers=2)
# ex.submit(wait_on_b)
# ex.submit(wait_on_a)