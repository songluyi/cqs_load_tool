# -*- coding: utf-8 -*-
# 2016/7/15 13:36
"""
-------------------------------------------------------------------------------
Function:   database of cqs_index
Version:    1.0
Author:     SLY
Contact:    slysly759@gmail.com 
 
-------------------------------------------------------------------------------
"""
import cx_Oracle
from openpyxl import load_workbook

def get_indexid():
    conn = cx_Oracle.connect("apps/apps@192.168.15.94:1539/NRCRP2")
    cur =conn.cursor()
    r= cur.execute("select t.index_id from CUX.CUX_CQS_INDEX_T t")
    index_id=[]
    for row in cur:
        index_id.extend(row)
    print('数据库中最大的Index_ID为')
    print(max(index_id))
    return max(index_id)

def get_batch_id():
    conn = cx_Oracle.connect("apps/apps@192.168.15.94:1539/NRCRP2")
    cur =conn.cursor()
    r= cur.execute("select t.batch_id from CUX.CUX_CQS_INDEX_T t")
    result=cur.fetchone()
    new_result=list(result)
    return new_result[0]

def compliment():
    header_name=['INDEX_ID', 'INDEX_ORDER', 'CATAGORY', 'SERVICES', 'DESIGN_TEMP_SOURCE', 'DESIGN_TEMP_MIN',
             'DESIGN_TEMP_MAX', 'DESIGN_TEMP_SPEC', 'DESIGN_PRES_SOURCE', 'DESIGN_PRES_MIN',
             'DESIGN_PRES_MAX', 'DESIGN_PRES_SPEC', 'PIPING_MATL_CLASS', 'BASIC_MATERIAL', 'RATING',
             'FLANGE_FACING', 'CA', 'NOTE', 'BATCH_ID', 'CREATED_BY', 'CREATION_DATE', 'LAST_UPDATED_BY',
             'LAST_UPDATE_DATE', 'LAST_UPDATE_LOGIN', 'ATTRIBUTE_CATEGORY', 'ATTRIBUTE1', 'ATTRIBUTE2',
             'ATTRIBUTE3', 'ATTRIBUTE4', 'ATTRIBUTE5', 'ATTRIBUTE6', 'ATTRIBUTE7', 'ATTRIBUTE8', 'ATTRIBUTE9',
             'ATTRIBUTE10', 'ATTRIBUTE11', 'ATTRIBUTE12', 'ATTRIBUTE13', 'ATTRIBUTE14', 'ATTRIBUTE15']
    name='new索引表.xlsx'
    wb_get_excel = load_workbook(filename=name)
    sheets = wb_get_excel.get_sheet_names()
    ws_get_excel = wb_get_excel.get_sheet_by_name(sheets[0])
    line=1
    while ws_get_excel.cell(row=line, column=1).value is not None:
       excel_data=[]
       line=line+1
       for column in range(1,len(header_name)+1):#循环取列值
           excel_data.append(ws_get_excel.cell(row=line, column=column).value)
           if  isinstance(ws_get_excel.cell(row=line, column=column).value, int):#判定值如果为int类型改为float更符合oracle
               excel_data[column-1]=float(excel_data[column-1])
       make_dict=dict(zip(header_name,excel_data))
       print(make_dict)
       print(len(make_dict))
       row=tuple(excel_data)
       new_row=[]
       new_row.append(row)
       def insert_db(header_name,row):
            conn = cx_Oracle.connect("apps/apps@192.168.15.94:1539/NRCRP2")
            cur =conn.cursor()
            db_name='CUX.CUX_CQS_INDEX_T'
            r= cur.execute(" INSERT INTO CUX.CUX_CQS_INDEX_T values (:INDEX_ID,:INDEX_ORDER,:CATAGORY,:SERVICES,:DESIGN_TEMP_SOURCE,:DESIGN_TEMP_MIN,:DESIGN_TEMP_MAX,:DESIGN_TEMP_SPEC,:DESIGN_PRES_SOURCE,:DESIGN_PRES_MIN,:DESIGN_PRES_MAX,:DESIGN_PRES_SPEC,:PIPING_MATL_CLASS,:BASIC_MATERIAL,:RATING,:FLANGE_FACING,:CA,:NOTE,:BATCH_ID,:CREATED_BY,TO_DATE(:CREATION_DATE,'yyyy/mm/dd'),:LAST_UPDATED_BY,TO_DATE(:LAST_UPDATE_DATE,'yyyy/mm/dd'),:LAST_UPDATE_LOGIN,:ATTRIBUTE_CATEGORY,:ATTRIBUTE1,:ATTRIBUTE2,:ATTRIBUTE3,:ATTRIBUTE4,:ATTRIBUTE5,:ATTRIBUTE6,:ATTRIBUTE7,:ATTRIBUTE8,:ATTRIBUTE9,:ATTRIBUTE10,:ATTRIBUTE11,:ATTRIBUTE12,:ATTRIBUTE13,:ATTRIBUTE14,:ATTRIBUTE15)", row)
            conn.commit()
       #这里因为多出来一条数据 想了一个本方法if判断了一下
       if make_dict['INDEX_ID'] is not None:
           insert_db(header_name,make_dict)
           print('插入了一条数据')



