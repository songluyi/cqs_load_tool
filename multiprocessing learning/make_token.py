# -*- coding: utf-8 -*-
# 2016/7/27 17:27
"""
-------------------------------------------------------------------------------
Function:
Version:    1.0
Author:     SLY
Contact:    slysly759@gmail.com 
 
-------------------------------------------------------------------------------
"""
# times:测试次数
# func: 要测试的函数名称
# 此方法是入口方法
# 各个算法以函数的形式定义，接受times参数即可——By MitchellChu
def crash_testx(times, func):
    import time
    print('\r\n--------------------------------------------')
    print("test function: %s" % func.func_name)
    print("begin time: %s" % time.strftime('%Y%m%d %X'))
    begin_time = time.time()
    (crashed_times, hash_data_len) = func(times)
    print("end time: %s" % time.strftime('%Y%m%d %X'))
    print("take time:%s" % (time.time() - begin_time))
    print("test times: %d, crashed times:%d, hash data length:%d" % (times, crashed_times, hash_data_len))
    print('--------------------------------------------\r\n')


