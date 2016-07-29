# -*- coding: utf-8 -*-
# 2016/7/28 16:42
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

def get_noteid():
    conn = cx_Oracle.connect("apps/apps@192.168.15.94:1539/NRCRP2")
    cur =conn.cursor()
    r= cur.execute("select note_id from cux.cux_cqs_notes_his_t")
    pt_id=[]
    for row in cur:
        pt_id.extend(row)
    print('数据库中最大的Note_ID为')
    print(max(pt_id))
    return max(pt_id)
def get_batch_id():
    conn = cx_Oracle.connect("apps/apps@192.168.15.94:1539/NRCRP2")
    cur =conn.cursor()
    r= cur.execute("select max(batch_id) from cux.cux_cqs_notes_his_t")
    result=cur.fetchone()
    new_result=list(result)
    return new_result[0]

def insert_db(row):
    conn = cx_Oracle.connect("apps/apps@192.168.15.94:1539/NRCRP2")
    cur =conn.cursor()
    r=cur.execute("truncate table cux.cux_cqs_notes_t")
    r=cur.executemany(" INSERT INTO cux.cux_cqs_notes_t values (:NOTE_ID,:SERVICE_SOURCE,:NOTE_KEY,:NOTE,:BATCH_ID,:CREATED_BY,to_date(:CREATION_DATE,'yyyy/mm/dd'),:LAST_UPDATED_BY,to_date(:LAST_UPDATE_DATE,'yyyy/mm/dd'),:LAST_UPDATE_LOGIN,:ATTRIBUTE_CATEGORY,:ATTRIBUTE1,:ATTRIBUTE2,:ATTRIBUTE3,:ATTRIBUTE4,:ATTRIBUTE5,:ATTRIBUTE6,:ATTRIBUTE7,:ATTRIBUTE8,:ATTRIBUTE9,:ATTRIBUTE10,:ATTRIBUTE11,:ATTRIBUTE12,:ATTRIBUTE13,:ATTRIBUTE14,:ATTRIBUTE15)", row)
    r=cur.execute("insert into cux.cux_cqs_notes_his_t select * from cux.cux_cqs_notes_t")
    conn.commit()
    print('数据已经导入成功')