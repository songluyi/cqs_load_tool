# -*- coding: utf-8 -*-
# 2016/8/4 15:19
"""
-------------------------------------------------------------------------------
Function:   删除备份文件
Version:    1.0
Author:     SLY
Contact:    slysly759@gmail.com 
 
-------------------------------------------------------------------------------
"""
import cx_Oracle
from recover_db import get_valid_batchid,get_batch

def delete_batch(re_batch):
    #合成各个SQL插入语句
    sql_index='delete CUX.CUX_CQS_INDEX_HIS_T where batch_id='+str(re_batch)
    sql_item='delete cux.cux_cqs_items_his_t  where batch_id='+str(re_batch)
    sql_pt_rating='delete cux.cux_cqs_pt_rating_his_t where batch_id='+str(re_batch)
    sql_pipe_thickness='delete cux.cux_cqs_pipe_thickness_his_t where batch_id='+str(re_batch)
    sql_connection='delete CUX.CUX_CQS_BRANCH_CONNECT_HIS_T where batch_id='+str(re_batch)
    sql_note='delete cux.cux_cqs_notes_his_t where batch_id='+str(re_batch)
    sql_batch='delete cux.cux_cqs_batchs_t where batch_id='+str(re_batch)
    conn = cx_Oracle.connect("apps/apps@192.168.15.94:1539/NRCRP2")
    cur =conn.cursor()
    #先执行清空数据语句
    r=cur.execute(sql_index)
    r=cur.execute(sql_item)
    r=cur.execute(sql_pt_rating)
    r=cur.execute(sql_pipe_thickness)
    r=cur.execute(sql_connection)
    r=cur.execute(sql_note)
    r=cur.execute(sql_batch)
    conn.commit()
    print('数据已经删除成功')
if __name__ == '__main__':
    batch_list=get_batch()
    valid_batchid=get_valid_batchid()
    print('\n'+'当前有效批次为：',valid_batchid,'\n')
    print("历史批次如下：")
    for batch in batch_list:
        print('批次号：',batch[0],'备注：',batch[1],'录入人：',batch[2],'时间：',batch[3])
    print('\n'+'1.单个删除仅输入他的批次号即可，如数字6')
    print('2.删除连续批次，如6-9\n'+'3.删除不连续批次请用逗号隔开，如6,8,9'+'\n')
    del_batch=input('请输入你需要删除的批次号：')
    if '-' in del_batch:
        batches=del_batch.split('-')
        for batch_id in range(int(batches[0]),int(batches[1])+1):
            delete_batch(batch_id)
    elif ',' in del_batch:
        batches=del_batch.split(',')
        for batch_id in batches:
            delete_batch(batch_id)
    elif isinstance(del_batch,int):
        delete_batch(del_batch)
    else:
        print('输入错误')

