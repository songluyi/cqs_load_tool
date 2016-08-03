# -*- coding: utf-8 -*-
# 2016/8/3 15:49
"""
-------------------------------------------------------------------------------
Function:
Version:    1.0
Author:     SLY
Contact:    slysly759@gmail.com 
 
-------------------------------------------------------------------------------
"""
# Test01_管道材料等级索引表.xlsx
# import os
# current_path=os.path.abspath(os.path.join(os.path.dirname('cqs_index.py'),os.path.pardir))
# new_path=current_path+'\\'+'excel\\'
# print(new_path)
#
# def get_path():
#     import os
#     current_path=os.path.abspath(os.path.join(os.path.dirname('cqs_index.py'),os.path.pardir))
#     new_path=current_path+'\\'+'excel\\'
#     FileList = []
#     rootdir = new_path
#
#     for root, subFolders, files in os.walk(rootdir):
#         #排除特定的子目录
#         if 'done' in subFolders:
#             subFolders.remove('done')
#         #查找特定扩展名的文件，只要包含'索引表'但不包含"new"字符串的文件，都会被包含
#         for f in files:
#             if f.find('等级表') != -1 and f.find('new')==-1:
#                 FileList.append(os.path.join(root, f))
#     for item in FileList:
#         print('检测到您目录下有如下excel文件 请确保他们是要提交的管道等级表')
#         print(item)
#     return FileList
# namelist=get_path()
# print(namelist)
import time,os,shutil
from cqs_branch_connect_database import get_batch_id
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
# today_time=time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
# new_ftp_path=str(today_time)+' '+str(get_batch_id())
# remotepath='/'+new_ftp_path+'/'
# file_path='\\backup\\'+new_ftp_path
# os.mkdir(file_path)
# base_path=os.getcwd()
# backup_excel_path=base_path.replace('bin','2016-08-03 16-26-53 10')
# backup_path=base_path.replace('bin','backup')
# shutil.move(backup_excel_path,backup_path)

