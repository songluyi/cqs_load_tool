# -*- coding: utf-8 -*-
# 2016/7/19 19:28
"""
-------------------------------------------------------------------------------
Function:   database of item
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
def get_itemid():
    conn = cx_Oracle.connect(db_connect)
    cur =conn.cursor()
    r= cur.execute("select max(item_id) from cux.cux_cqs_items_his_t")
    result=cur.fetchone()
    new_result=list(result)
    return new_result[0]
def get_batch_id():
    conn = cx_Oracle.connect(db_connect)
    cur =conn.cursor()
    r= cur.execute("select max(batch_id) from cux.cux_cqs_items_his_t")
    result=cur.fetchone()
    new_result=list(result)
    return new_result[0]

def get_order_number():
    conn = cx_Oracle.connect(db_connect)
    cur =conn.cursor()
    r= cur.execute("select max(item_order_number) from cux.cux_cqs_items_his_t")
    result=cur.fetchone()
    new_result=list(result)
    return new_result[0]
def insert_db(row):
    conn = cx_Oracle.connect(db_connect)
    cur =conn.cursor()
    r=cur.execute("truncate table cux.cux_cqs_items_t")
    r=cur.executemany(" INSERT INTO cux.cux_cqs_items_t values (:ITEM_ID,:BATCH_ID,:ITEM_ORDER_NUMBER,:PIPING_MATL_CLASS,:ITEM_CATEGORY,:ITEM_NAME,:MIN_DN,:MAX_DN,:END_FACING,:THK_RATING,:MATERIAL,:STANDARD_MODEL,:NOTE,:CREATED_BY,to_date(:CREATION_DATE,'yyyy/mm/dd'),:LAST_UPDATED_BY,to_date(:LAST_UPDATE_DATE,'yyyy/mm/dd'),:LAST_UPDATE_LOGIN,:ATTRIBUTE_CATEGORY,:ATTRIBUTE1,:ATTRIBUTE2,:ATTRIBUTE3,:ATTRIBUTE4,:ATTRIBUTE5,:ATTRIBUTE6,:ATTRIBUTE7,:ATTRIBUTE8,:ATTRIBUTE9,:ATTRIBUTE10,:ATTRIBUTE11,:ATTRIBUTE12,:ATTRIBUTE13,:ATTRIBUTE14,:ATTRIBUTE15)", row)
    r=cur.execute("insert into  cux.cux_cqs_items_his_t select * from cux.cux_cqs_items_t")
    conn.commit()
    print('数据已经导入成功')


