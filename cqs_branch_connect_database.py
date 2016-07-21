# -*- coding: utf-8 -*-
# 2016/7/20 15:37
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
def get_connectionid():
    conn = cx_Oracle.connect("apps/apps@192.168.15.94:1539/NRCRP2")
    cur =conn.cursor()
    r= cur.execute("select connection_id from CUX.CUX_CQS_BRANCH_CONNECT_T")
    pt_id=[]
    for row in cur:
        pt_id.extend(row)
    print('数据库中最大的PT_ID为')
    print(max(pt_id))
    return max(pt_id)

def get_batch_id():
    conn = cx_Oracle.connect("apps/apps@192.168.15.94:1539/NRCRP2")
    cur =conn.cursor()
    r= cur.execute("select batch_id from CUX.CUX_CQS_BRANCH_CONNECT_T")
    result=cur.fetchone()
    new_result=list(result)
    return new_result[0]

def get_order_number():
    conn = cx_Oracle.connect("apps/apps@192.168.15.94:1539/NRCRP2")
    cur =conn.cursor()
    r= cur.execute("select conn_order_number from CUX.CUX_CQS_BRANCH_CONNECT_T")
    conn_id=[]
    for row in cur:
        conn_id.extend(row)
    print('数据库中最大的conn_order_number为')
    print(max(conn_id))
    return max(conn_id)


def compliment():
    header_name=['CONNECTION_ID', 'BATCH_ID', 'CONN_ORDER_NUMBER', 'PIPING_MATL_CLASS', 'BRANCH_DN',
             'HEADER_DN', 'CONNECTION_TYPE', 'CREATED_BY', 'CREATION_DATE', 'LAST_UPDATED_BY',
             'LAST_UPDATE_DATE', 'LAST_UPDATE_LOGIN', 'ATTRIBUTE_CATEGORY', 'ATTRIBUTE1', 'ATTRIBUTE2',
             'ATTRIBUTE3', 'ATTRIBUTE4', 'ATTRIBUTE5', 'ATTRIBUTE6', 'ATTRIBUTE7', 'ATTRIBUTE8',
             'ATTRIBUTE9', 'ATTRIBUTE10', 'ATTRIBUTE11', 'ATTRIBUTE12', 'ATTRIBUTE13', 'ATTRIBUTE14',
             'ATTRIBUTE15']
    name='new管道连接.xlsx'
    wb_get_excel = load_workbook(filename=name)
    sheets = wb_get_excel.get_sheet_names()
    ws_get_excel = wb_get_excel.get_sheet_by_name(sheets[0])
    line=2
    while ws_get_excel.cell(row=line, column=1).value is not None:
       excel_data=[]
       for column in range(1,len(header_name)+1):#循环取列值
           excel_data.append(ws_get_excel.cell(row=line, column=column).value)
           if  isinstance(ws_get_excel.cell(row=line, column=column).value, int):#判定值如果为int类型改为float更符合oracle
               excel_data[column-1]=float(excel_data[column-1])
       make_dict=dict(zip(header_name,excel_data))
       line=line+1
       print(make_dict)
       def insert_db(header_name,row):
            conn = cx_Oracle.connect("apps/apps@192.168.15.94:1539/NRCRP2")
            cur =conn.cursor()
            # db_name='CUX.CUX_CQS_INDEX_T'
            r= cur.execute(" INSERT INTO CUX.CUX_CQS_BRANCH_CONNECT_T values (:CONNECTION_ID,:BATCH_ID,:CONN_ORDER_NUMBER,:PIPING_MATL_CLASS,:BRANCH_DN,:HEADER_DN,:CONNECTION_TYPE,:CREATED_BY,to_date(:CREATION_DATE,'yyyy/mm/dd'),:LAST_UPDATED_BY,to_date(:LAST_UPDATE_DATE,'yyyy/mm/dd'),:LAST_UPDATE_LOGIN,:ATTRIBUTE_CATEGORY,:ATTRIBUTE1,:ATTRIBUTE2,:ATTRIBUTE3,:ATTRIBUTE4,:ATTRIBUTE5,:ATTRIBUTE6,:ATTRIBUTE7,:ATTRIBUTE8,:ATTRIBUTE9,:ATTRIBUTE10,:ATTRIBUTE11,:ATTRIBUTE12,:ATTRIBUTE13,:ATTRIBUTE14,:ATTRIBUTE15)", row)
            conn.commit()
       insert_db(header_name,make_dict)
       print('插入了一条数据')


