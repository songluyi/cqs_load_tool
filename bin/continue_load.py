# -*- coding: utf-8 -*-
# 2016/8/1 15:35
"""
-------------------------------------------------------------------------------
Function:   实现断点续传功能
Version:    1.0
Author:     SLY
Contact:    slysly759@gmail.com 
 
-------------------------------------------------------------------------------
"""
import cx_Oracle
from cqs_pt_rating_database import get_ini
db_connect=get_ini()[0]
def get_batch_id():
    conn = cx_Oracle.connect(db_connect)
    cur =conn.cursor()
    r= cur.execute("select max(batch_id) from CUX.CUX_CQS_BRANCH_CONNECT_HIS_T")
    result=cur.fetchone()
    new_result=list(result)
    return new_result[0]
def continue_load_db():
    conn = cx_Oracle.connect(db_connect)
    cur =conn.cursor()
    del_batch_id=get_batch_id()
    change_batch_id=del_batch_id-1
    sql_index='update CUX.CUX_CQS_INDEX_HIS_T set batch_id='+str(change_batch_id)+'where batch_id='+str(del_batch_id)
    sql_item='update cux.cux_cqs_items_his_t set batch_id='+str(change_batch_id)+'where batch_id='+str(del_batch_id)
    sql_pt_rating='update cux.cux_cqs_pt_rating_his_t set batch_id='+str(change_batch_id)+'where batch_id='+str(del_batch_id)
    sql_thickness='update cux.cux_cqs_pipe_thickness_his_t set batch_id='+str(change_batch_id)+'where batch_id='+str(del_batch_id)
    sql_connect='update CUX.CUX_CQS_BRANCH_CONNECT_HIS_T set batch_id='+str(change_batch_id)+'where batch_id='+str(del_batch_id)
    sql_note='update cux.cux_cqs_notes_his_t set batch_id='+str(change_batch_id)+'where batch_id='+str(del_batch_id)
    # sql_batchs='update cux.cux_cqs_batchs_his_t set batch_id='+str(change_batch_id)+'where batch_id='+str(get_batch_id())
    r=cur.execute(sql_index)
    r=cur.execute(sql_item)
    r=cur.execute(sql_pt_rating)
    r=cur.execute(sql_thickness)
    r=cur.execute(sql_connect)
    r=cur.execute(sql_note)
    # r=cur.execute(sql_batchs)
    #先执行清空数据语句
    r=cur.execute('truncate table CUX.CUX_CQS_INDEX_T')
    r=cur.execute('truncate table cux.cux_cqs_items_t')
    r=cur.execute('truncate table cux.cux_cqs_pt_rating_t')
    r=cur.execute('truncate table cux.cux_cqs_pipe_thickness_t')
    r=cur.execute('truncate table CUX.CUX_CQS_BRANCH_CONNECT_T')
    r=cur.execute('truncate table cux.cux_cqs_notes_t')
    #合成各个SQL插入语句
    sql_index='insert into CUX.CUX_CQS_INDEX_T select * from CUX.CUX_CQS_INDEX_HIS_T where batch_id='+str(change_batch_id)
    sql_item='insert into cux.cux_cqs_items_t select * from cux.cux_cqs_items_his_t where batch_id='+str(change_batch_id)
    sql_pt_rating='insert into cux.cux_cqs_pt_rating_t select * from cux.cux_cqs_pt_rating_his_t where batch_id='+str(change_batch_id)
    sql_pipe_thickness='insert into cux.cux_cqs_pipe_thickness_t select * from cux.cux_cqs_pipe_thickness_his_t where batch_id='+str(change_batch_id)
    sql_connection='insert into CUX.CUX_CQS_BRANCH_CONNECT_T select * from CUX.CUX_CQS_BRANCH_CONNECT_HIS_T where batch_id='+str(change_batch_id)
    sql_note='insert into cux.cux_cqs_notes_t select * from cux.cux_cqs_notes_his_t where batch_id='+str(change_batch_id)
    sql_batch='delete cux.cux_cqs_batchs_t where batch_id='+str(del_batch_id)
    r=cur.execute(sql_index)
    r=cur.execute(sql_item)
    r=cur.execute(sql_pt_rating)
    r=cur.execute(sql_pipe_thickness)
    r=cur.execute(sql_connection)
    r=cur.execute(sql_note)
    r=cur.execute(sql_batch)
    conn.commit()
    print('数据续传成功')
if __name__ == '__main__':
    continue_load_db()