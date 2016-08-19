# -*- coding: utf-8 -*-
# 2016/7/20 15:36
"""
-------------------------------------------------------------------------------
Function:   支管连接表插入数据库主程序
Version:    1.0
Author:     SLY
Contact:    slysly759@gmail.com 
 
-------------------------------------------------------------------------------
"""
import os,sys
from openpyxl import Workbook
from openpyxl import load_workbook
from cqs_branch_connect_database import *
import threading
from cqs_pt_rating import cqs_pt_rating#这里主要为了引入get_path函数
from cqs_pt_rating_database import compliment
# from concurrent import futures#采用3.x新出来的多进程
import time
today_time=time.strftime("%Y-%m-%d", time.localtime())
today_time=today_time.replace('-','/')
header_name=['CONNECTION_ID', 'BATCH_ID', 'CONN_ORDER_NUMBER', 'PIPING_MATL_CLASS', 'BRANCH_DN',
             'HEADER_DN', 'CONNECTION_TYPE', 'CREATED_BY', 'CREATION_DATE', 'LAST_UPDATED_BY',
             'LAST_UPDATE_DATE', 'LAST_UPDATE_LOGIN', 'ATTRIBUTE_CATEGORY', 'ATTRIBUTE1', 'ATTRIBUTE2',
             'ATTRIBUTE3', 'ATTRIBUTE4', 'ATTRIBUTE5', 'ATTRIBUTE6', 'ATTRIBUTE7', 'ATTRIBUTE8',
             'ATTRIBUTE9', 'ATTRIBUTE10', 'ATTRIBUTE11', 'ATTRIBUTE12', 'ATTRIBUTE13', 'ATTRIBUTE14',
             'ATTRIBUTE15']
class cqs_branch_connect(object):

    def make_exceldata(self,name_list,bug_connection_id,connection_id,batch_id,conn_order_number):
        wb_write=Workbook()
        ws_write = wb_write.get_active_sheet()
        ws_write.title = 'pt_rating'
        line=1#从第二行开始
        connection_id=connection_id+1
        batch_id=batch_id+1
        conn_order_number=conn_order_number+1
        for i in range(1,29):
                ws_write.cell(row=1, column=i).value = header_name[i-1]
        for name in name_list:
            # load_name=os.path.basename(name)
            if bug_connection_id>connection_id:#因为读取不同的excel，此时数据库中还没有同步插入 必须要用一个bug_pipe_id来解决下一个文件的pipe_id的取值问题
                connection_id=bug_connection_id
            wb_load = load_workbook(filename=name)
            sheets = wb_load.get_sheet_names()
            del sheets[-1]#用openpyxl这个模块获取excel标签尾部会多一个页签，具体原因不明
            for page_name in sheets[1::2]:#循环样例应该为16.2 35.2 等
                ws_load = wb_load.get_sheet_by_name(page_name)
                check_row_lines=[]
                for row in range(14,45):
                    if isinstance(ws_load.cell(row=row, column=3).value,int):
                        check_row_lines.append(row)
                check_row=min(check_row_lines)
                max_column=5+max(check_row_lines)-check_row
                for column in range(5,max_column+1):
                    count=column-4
                    for row in range(check_row+count-1,44):
                        connection_id+=1
                        conn_order_number+=1
                        line+=1
                        bug_connection_id+=1
                        ws_write.cell(row=line, column=1).value=connection_id
                        ws_write.cell(row=line, column=2).value=batch_id
                        ws_write.cell(row=line, column=3).value=conn_order_number
                        ws_write.cell(row=line, column=4).value=ws_load.cell(row=1, column=26).value#写入metal class
                        ws_write.cell(row=line, column=5).value=ws_load.cell(row=44, column=column).value   #写入主管
                        # print(row,column)
                        ws_write.cell(row=line, column=6).value=ws_load.cell(row=row, column=3).value   #写入支管
                        ws_write.cell(row=line, column=7).value=ws_load.cell(row=row, column=column).value  #连接方式
                        ws_write.cell(row=line, column=8).value=0#写入created by
                        ws_write.cell(row=line, column=9).number_format='yyyy-mm-dd'
                        ws_write.cell(row=line, column=9).value=today_time
                        ws_write.cell(row=line, column=10).value=0#写入last_update_by
                        ws_write.cell(row=line, column=11).number_format='yyyy-mm-dd'
                        ws_write.cell(row=line, column=11).value=today_time
                        ws_write.cell(row=line, column=12).value=0#写入last_update_login
        name='new'+'管道连接'+'.xlsx'
        wb_write.save(name)
        print('已经完成管道连接表的excel生成')

if __name__ == '__main__':
    cqs=cqs_branch_connect()
    name_list=cqs_pt_rating().get_path()
    connection_id=get_connectionid()
    if connection_id is None:
        connection_id=0
    batch_id=get_batch_id()
    if batch_id is None:
        batch_id=0
    conn_order_number=get_order_number()
    if conn_order_number is None:
        conn_order_number=0
    bug_connection_id=0
    cqs.make_exceldata(name_list,bug_connection_id,connection_id,batch_id,conn_order_number)
    excel_name='new管道连接.xlsx'
    data_list=compliment(header_name,excel_name)
    start_time=time.time()
    insert_db(data_list)
    end_time=time.time()
    print('耗时为：',end_time-start_time,'插入总数为：',len(data_list))
    print('已经完成对管道连接表的插入，谢谢使用')
    insert_batch_db(today_time)





