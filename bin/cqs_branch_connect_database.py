# -*- coding: utf-8 -*-
# 2016/7/20 15:37
"""
-------------------------------------------------------------------------------
Function:   支管连接表的数据库程序
Version:    1.0
Author:     SLY
Contact:    slysly759@gmail.com 
 
-------------------------------------------------------------------------------
"""

import cx_Oracle,os
from openpyxl import load_workbook
from cqs_pt_rating_database import get_ini
db_connect=get_ini()[0]
# 设置编码，否则：
# 1. Oracle 查询出来的中文是乱码
# 2. 插入数据时有中文，会导致
# UnicodeEncodeError: 'ascii' codec can't encode characters in position 1-7: ordinal not in range(128)
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

def get_connectionid():
    conn = cx_Oracle.connect(db_connect)
    cur =conn.cursor()
    r= cur.execute("select max(connection_id) from CUX.CUX_CQS_BRANCH_CONNECT_HIS_T")
    result=cur.fetchone()
    new_result=list(result)
    return new_result[0]

def get_batch_id():
    conn = cx_Oracle.connect(db_connect)
    cur =conn.cursor()
    r= cur.execute("select max(batch_id) from CUX.CUX_CQS_BRANCH_CONNECT_HIS_T")
    result=cur.fetchone()
    new_result=list(result)
    return new_result[0]

def get_order_number():
    conn = cx_Oracle.connect(db_connect)
    cur =conn.cursor()
    r= cur.execute("select max(conn_order_number) from CUX.CUX_CQS_BRANCH_CONNECT_HIS_T")
    result=cur.fetchone()
    new_result=list(result)
    return new_result[0]

def insert_db(row):
    conn = cx_Oracle.connect(db_connect)
    cur =conn.cursor()
    r=cur.execute("truncate table CUX.CUX_CQS_BRANCH_CONNECT_T")
    r=cur.executemany(" INSERT INTO CUX.CUX_CQS_BRANCH_CONNECT_T values (:CONNECTION_ID,:BATCH_ID,:CONN_ORDER_NUMBER,:PIPING_MATL_CLASS,:BRANCH_DN,:HEADER_DN,:CONNECTION_TYPE,:CREATED_BY,to_date(:CREATION_DATE,'yyyy/mm/dd'),:LAST_UPDATED_BY,to_date(:LAST_UPDATE_DATE,'yyyy/mm/dd'),:LAST_UPDATE_LOGIN,:ATTRIBUTE_CATEGORY,:ATTRIBUTE1,:ATTRIBUTE2,:ATTRIBUTE3,:ATTRIBUTE4,:ATTRIBUTE5,:ATTRIBUTE6,:ATTRIBUTE7,:ATTRIBUTE8,:ATTRIBUTE9,:ATTRIBUTE10,:ATTRIBUTE11,:ATTRIBUTE12,:ATTRIBUTE13,:ATTRIBUTE14,:ATTRIBUTE15)", row)
    r=cur.execute("insert into  CUX.CUX_CQS_BRANCH_CONNECT_HIS_T select * from CUX.CUX_CQS_BRANCH_CONNECT_T")
    conn.commit()
    print('数据已经导入成功')
def del_rest_data(sql_str):
    conn = cx_Oracle.connect(db_connect)
    cur =conn.cursor()
    r=cur.execute(sql_str)
    conn.commit()
def make_sql_str(min_batch_id):
    sql_name=['CUX.CUX_CQS_INDEX_HIS_T','cux.cux_cqs_items_his_t','cux.cux_cqs_pt_rating_his_t','cux.cux_cqs_pipe_thickness_his_t'
    ,'CUX.CUX_CQS_BRANCH_CONNECT_HIS_T','cux.cux_cqs_notes_his_t']
    sql_list=[]
    for name in sql_name:
        sql_command='delete from %s where batch_id>%s'%(name,min_batch_id)
        sql_list.append(sql_command)
    return sql_list
def insert_batch_db(today_time):
    import getpass
    header_name=['BATCH_ID', 'COMMENTS', 'CREATION_DATE', 'LAST_UPDATE_DATE', 'CREATED_BY',
                 'LAST_UPDATED_BY', 'LAST_UPDATE_LOGIN', 'ATTRIBUTE_CATEGORY', 'ATTRIBUTE1', 'ATTRIBUTE2',
                 'ATTRIBUTE3', 'ATTRIBUTE4', 'ATTRIBUTE5', 'ATTRIBUTE6', 'ATTRIBUTE7', 'ATTRIBUTE8',
                 'ATTRIBUTE9', 'ATTRIBUTE10', 'ATTRIBUTE11', 'ATTRIBUTE12', 'ATTRIBUTE13',
                 'ATTRIBUTE14', 'ATTRIBUTE15']
    COMMENTS='Nerin Load'+str(today_time)
    BATCH_ID=get_batch_id()
    CREATION_DATE=today_time;LAST_UPDATE_DATE=today_time
    data=[]
    CREATED_BY=0;LAST_UPDATED_BY=0
    LAST_UPDATE_LOGIN=1
    ATTRIBUTE_CATEGORY=getpass.getuser()
    data.append(BATCH_ID);data.append(COMMENTS);data.append(CREATION_DATE);data.append(LAST_UPDATE_DATE)
    data.append(CREATED_BY);data.append(LAST_UPDATED_BY);data.append(LAST_UPDATE_LOGIN);data.append(ATTRIBUTE_CATEGORY)#目前没想到追加的好方式，打算自己造一个轮子批量append
    row=dict(zip(header_name,data))
    print(row)
    conn = cx_Oracle.connect(db_connect)
    cur =conn.cursor()
    r=cur.execute(" insert into cux.cux_cqs_batchs_t(BATCH_ID,COMMENTS,CREATION_DATE,LAST_UPDATE_DATE,CREATED_BY,LAST_UPDATED_BY,LAST_UPDATE_LOGIN,ATTRIBUTE_CATEGORY) values (:BATCH_ID,:COMMENTS,to_date(:CREATION_DATE,'yyyy/mm/dd'),to_date(:LAST_UPDATE_DATE,'yyyy/mm/dd'),:CREATED_BY,:LAST_UPDATED_BY,:LAST_UPDATE_LOGIN,:ATTRIBUTE_CATEGORY)", row)
    conn.commit()
    COMMENTS=input('请输入一段描述方便自己日后恢复数据,如果是续传请随意填写不会导入到数据库,填写后记得回车:')
    conn = cx_Oracle.connect(db_connect)
    cur =conn.cursor()
    sql="UPDATE cux.cux_cqs_batchs_t set comments='%s' where batch_id=%s"%(COMMENTS,BATCH_ID)
    r=cur.execute(sql)
    conn.commit()
    print('数据已经导入成功')











