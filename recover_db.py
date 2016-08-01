# -*- coding: utf-8 -*-
# 2016/7/29 14:42
"""
-------------------------------------------------------------------------------
Function:   用于数据库的恢复
Version:    1.0
Author:     SLY
Contact:    slysly759@gmail.com 
 
-------------------------------------------------------------------------------
"""
import cx_Oracle
def get_batch():
    conn = cx_Oracle.connect("apps/apps@192.168.15.94:1539/NRCRP2")
    cur =conn.cursor()
    r=cur.execute("select batch_id,comments,creation_date from cux.cux_cqs_batchs_t order by batch_id")
    result=cur.fetchall()
    return result

def recover_batch(re_batch):
    #合成各个SQL插入语句
    sql_index='insert into CUX.CUX_CQS_INDEX_T select * from CUX.CUX_CQS_INDEX_HIS_T where batch_id='+str(re_batch)
    sql_item='insert into cux.cux_cqs_items_t select * from cux.cux_cqs_items_his_t where batch_id='+str(re_batch)
    sql_pt_rating='insert into cux.cux_cqs_pt_rating_t select * from cux.cux_cqs_pt_rating_his_t where batch_id='+str(re_batch)
    sql_pipe_thickness='insert into cux.cux_cqs_pipe_thickness_t select * from cux.cux_cqs_pipe_thickness_his_t where batch_id='+str(re_batch)
    sql_connection='insert into CUX.CUX_CQS_BRANCH_CONNECT_T select * from CUX.CUX_CQS_BRANCH_CONNECT_HIS_T where batch_id='+str(re_batch)
    sql_note='insert into cux.cux_cqs_notes_t select * from cux.cux_cqs_notes_his_t where batch_id='+str(re_batch)
    conn = cx_Oracle.connect("apps/apps@192.168.15.94:1539/NRCRP2")
    cur =conn.cursor()
    #先执行清空数据语句
    r=cur.execute('truncate table CUX.CUX_CQS_INDEX_T')
    r=cur.execute('truncate table cux.cux_cqs_items_t')
    r=cur.execute('truncate table cux.cux_cqs_pt_rating_t')
    r=cur.execute('truncate table cux.cux_cqs_pipe_thickness_t')
    r=cur.execute('truncate table CUX.CUX_CQS_BRANCH_CONNECT_T')
    r=cur.execute('truncate table cux.cux_cqs_notes_t')
    r=cur.execute(sql_index)
    r=cur.execute(sql_item)
    r=cur.execute(sql_pt_rating)
    r=cur.execute(sql_pipe_thickness)
    r=cur.execute(sql_connection)
    r=cur.execute(sql_note)
    conn.commit()
    print('数据已经恢复成功')

batch_list=get_batch()
print("历史批次如下：")
for batch in batch_list:
    print('批次号：',batch[0],'批次备注信息：',batch[1],'录入时间：',batch[2])
re_batch=int(input('请输入你需要恢复的批次号：'))
recover_batch(re_batch)