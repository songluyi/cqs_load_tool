# -*- coding: utf-8 -*-
# 2016/7/19 19:28
"""
-------------------------------------------------------------------------------
Function:
Version:    1.0
Author:     SLY
Contact:    slysly759@gmail.com 
 
-------------------------------------------------------------------------------
"""
import cx_Oracle,random
from openpyxl import load_workbook

def get_itemid():
    conn = cx_Oracle.connect("apps/apps@192.168.15.94:1539/NRCRP2")
    cur =conn.cursor()
    r= cur.execute("select item_id from cux.cux_cqs_items_t")
    pt_id=[]
    for row in cur:
        pt_id.extend(row)
    print('数据库中最大的ITEM_ID为')
    print(max(pt_id))
    return max(pt_id)
def get_batch_id():
    conn = cx_Oracle.connect("apps/apps@192.168.15.94:1539/NRCRP2")
    cur =conn.cursor()
    r= cur.execute("select batch_id from cux.cux_cqs_items_t")
    result=cur.fetchone()
    new_result=list(result)
    return new_result[0]

def get_order_number():
    conn = cx_Oracle.connect("apps/apps@192.168.15.94:1539/NRCRP2")
    cur =conn.cursor()
    r= cur.execute("select item_order_number from cux.cux_cqs_items_t")
    item_id=[]
    for row in cur:
        item_id.extend(row)
    print('数据库中最大的item_order_number为')
    print(max(item_id))
    return max(item_id)
def insert_db(row):
    conn = cx_Oracle.connect("apps/apps@192.168.15.94:1539/NRCRP2")
    cur =conn.cursor()
    r= cur.executemany(" INSERT INTO cux.cux_cqs_items_t values (:ITEM_ID,:BATCH_ID,:ITEM_ORDER_NUMBER,:PIPING_MATL_CLASS,:ITEM_CATEGORY,:ITEM_NAME,:MIN_DN,:MAX_DN,:END_FACING,:THK_RATING,:MATERIAL,:STANDARD_MODEL,:NOTE,:CREATED_BY,to_date(:CREATION_DATE,'yyyy/mm/dd'),:LAST_UPDATED_BY,to_date(:LAST_UPDATE_DATE,'yyyy/mm/dd'),:LAST_UPDATE_LOGIN,:ATTRIBUTE_CATEGORY,:ATTRIBUTE1,:ATTRIBUTE2,:ATTRIBUTE3,:ATTRIBUTE4,:ATTRIBUTE5,:ATTRIBUTE6,:ATTRIBUTE7,:ATTRIBUTE8,:ATTRIBUTE9,:ATTRIBUTE10,:ATTRIBUTE11,:ATTRIBUTE12,:ATTRIBUTE13,:ATTRIBUTE14,:ATTRIBUTE15)", row)
    conn.commit()
    print('已经插入一条,如果发现本显示没有刷新请手动关掉，数据已经导入成功')


