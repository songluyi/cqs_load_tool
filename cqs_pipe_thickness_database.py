# -*- coding: utf-8 -*-
# 2016/7/20 13:38
"""
-------------------------------------------------------------------------------
Function:
Version:    1.0
Author:     SLY
Contact:    slysly759@gmail.com 
 
-------------------------------------------------------------------------------
"""
import cx_Oracle
from openpyxl import load_workbook
def get_pipeid():
    conn = cx_Oracle.connect("apps/apps@192.168.15.94:1539/NRCRP2")
    cur =conn.cursor()
    r= cur.execute("select pipe_id from cux.cux_cqs_pipe_thickness_t")
    pt_id=[]
    for row in cur:
        pt_id.extend(row)
    print('数据库中最大的PT_ID为')
    print(max(pt_id))
    return max(pt_id)
def get_batch_id():
    conn = cx_Oracle.connect("apps/apps@192.168.15.94:1539/NRCRP2")
    cur =conn.cursor()
    r= cur.execute("select batch_id from cux.cux_cqs_pipe_thickness_t")
    result=cur.fetchone()
    new_result=list(result)
    return new_result[0]
def get_order_number():
    conn = cx_Oracle.connect("apps/apps@192.168.15.94:1539/NRCRP2")
    cur =conn.cursor()
    r= cur.execute("select pipe_order_number from cux.cux_cqs_pipe_thickness_t")
    pipe_id=[]
    for row in cur:
        pipe_id.extend(row)
    print('数据库中最大的pipe_order_number为')
    print(max(pipe_id))
    return max(pipe_id)
def insert_db(row):
    conn = cx_Oracle.connect("apps/apps@192.168.15.94:1539/NRCRP2")
    cur =conn.cursor()
    r= cur.execute(" INSERT INTO cux.cux_cqs_pipe_thickness_t values (:PIPE_ID,:BATCH_ID,:PIPE_ORDER_NUMBER,:PIPING_MATL_CLASS,:PIPE_DN,:PIPE_OUTER,:PIPE_THICKNESS,:CREATED_BY,to_date(:CREATION_DATE,'yyyy/mm/dd'),:LAST_UPDATED_BY,to_date(:LAST_UPDATE_DATE,'yyyy/mm/dd'),:LAST_UPDATE_LOGIN,:ATTRIBUTE_CATEGORY,:ATTRIBUTE1,:ATTRIBUTE2,:ATTRIBUTE3,:ATTRIBUTE4,:ATTRIBUTE5,:ATTRIBUTE6,:ATTRIBUTE7,:ATTRIBUTE8,:ATTRIBUTE9,:ATTRIBUTE10,:ATTRIBUTE11,:ATTRIBUTE12,:ATTRIBUTE13,:ATTRIBUTE14,:ATTRIBUTE15)", row)
    conn.commit()
    print('success')


