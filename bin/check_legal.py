# -*- coding: utf-8 -*-
# 2016/8/3 18:14
"""
-------------------------------------------------------------------------------
Function:
Version:    1.0
Author:     SLY
Contact:    slysly759@gmail.com 
 
-------------------------------------------------------------------------------
"""
from about_ftp import get_path
from openpyxl import load_workbook
import cqs_index_database
import cqs_items_database
import cqs_note_database
import cqs_pipe_thickness_database
import cqs_pt_rating_database
import cqs_branch_connect_database
def check_batch_id():
    index_batch_id=cqs_index_database.get_batch_id()
    item_batch_id=cqs_items_database.get_batch_id()
    note_batch_id=cqs_note_database.get_batch_id()
    pipe_batch_id=cqs_pipe_thickness_database.get_batch_id()
    pt_rate_batch_id=cqs_pt_rating_database.get_batch_id()
    connect_batch_id=cqs_branch_connect_database.get_batch_id()
    print('索引表历史最大批次号',index_batch_id)
    print('元件表历史最大批次号',item_batch_id)
    print('注释表历史最大批次号',note_batch_id)
    print('壁厚表历史最大批次号',pipe_batch_id)
    print('压力温度表历史最大批次号',pt_rate_batch_id)
    print('支管连接批次号',connect_batch_id)
    if index_batch_id==item_batch_id==note_batch_id==pipe_batch_id==pt_rate_batch_id==connect_batch_id:
        print('目前所有批次号正常')
    else:
        print('批次号可能存在异常，原因可能是导入异常数据导致，请进入PLSQL界面操作，保证批次号相同')
namelist=get_path()
print(namelist)
for name in namelist:
    if '索引表' in name:
        error_time=0
        wb_load = load_workbook(filename=name)
        sheets = wb_load.get_sheet_names()
        ws_load = wb_load.get_sheet_by_name(sheets[0])
        if 'Services' in ws_load.cell(row=6, column=2).value:
            print('success')
            print('索引表符合导入要求')
        else:
            error_time+=1
        if error_time>0:
            print('索引表不符合要求')

    if '等级表' in name:
        error_time=0
        wb_load = load_workbook(filename=name)
        sheets = wb_load.get_sheet_names()
        del sheets[-1]#用openpyxl这个模块获取excel标签尾部会多一个页签，具体原因不明
        for page_name in sheets[::2]:#循环页签
            ws_load = wb_load.get_sheet_by_name(page_name)
            if '温度' in ws_load.cell(row=9, column=1).value and '压力' in ws_load.cell(row=10, column=1).value:
                if '元件名称' in ws_load.cell(row=11,column=1).value:
                    print('success')
            else:
                error_time+=1
        for page_name in sheets[1::2]:#循环页签
            ws_load = wb_load.get_sheet_by_name(page_name)
            if 'DN' in ws_load.cell(row=5, column=1).value and '外径' in ws_load.cell(row=6, column=1).value:
                if '主管' in ws_load.cell(row=45,column=5).value:
                    print('success')
            else:
                error_time+=1
        if error_time>0:
            print('等级表导入数据错误')
        else:
            print('等级表符合导入要求')

check_batch_id()




