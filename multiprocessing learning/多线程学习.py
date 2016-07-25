# -*- coding: utf-8 -*-
# 2016/7/21 16:35
"""
-------------------------------------------------------------------------------
Function:
Version:    1.0
Author:     SLY
Contact:    slysly759@gmail.com 
 
-------------------------------------------------------------------------------
"""

# from multiprocessing import Process
# import os
#
# # 子进程要执行的代码
# def run_proc(name):
#     print('Run child process %s (%s)...' % (name, os.getpid()))
#
# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Process(target=run_proc, args=('test',))
#     print('Child process will start.')
#     p.start()
#     p.join()
#     print('Child process end.')

# from multiprocessing import Pool
# import os, time, random
#
# def long_time_task(name):
#     print('Run task %s (%s)...' % (name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print('Task %s runs %0.2f seconds.' % (name, (end - start)))
#
# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,))
#     print('Waiting for all subprocesses done...')
#     p.close()
#     p.join()
#     print('All subprocesses done.')

# import subprocess
#
# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup', 'www.python.org'])
# print('Exit code:', r)

# import subprocess
#
# print('$ nslookup')
# p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
# print(output.decode('utf-8'))
# print('Exit code:', p.returncode)

# from multiprocessing import Process, Queue
# import os, time, random
#
# # 写数据进程执行的代码:
# def write(q):
#     print('Process to write: %s' % os.getpid())
#     for value in ['A', 'B', 'C']:
#         print('Put %s to queue...' % value)
#         q.put(value)
#         time.sleep(random.random())
#
# # 读数据进程执行的代码:
# def read(q):
#     print('Process to read: %s' % os.getpid())
#     while True:
#         value = q.get(True)
#         print('Get %s from queue.' % value)
#
# if __name__=='__main__':
#     # 父进程创建Queue，并传给各个子进程：
#     q = Queue()
#     pw = Process(target=write, args=(q,))
#     pr = Process(target=read, args=(q,))
#     # 启动子进程pw，写入:
#     pw.start()
#     # 启动子进程pr，读取:
#     pr.start()
#     # 等待pw结束:
#     pw.join()
#     # pr进程里是死循环，无法等待其结束，只能强行终止:
#     pr.terminate()

# from multiprocessing import Pool
# from multiprocessing.dummy import Pool as ThreadPool
# import time
# import urllib.request
#
# urls = [
#     'http://www.baidu.com',
#     'http://home.baidu.com/',
#     'http://tieba.baidu.com/',
#     'http://zhidao.baidu.com/',
#     'http://music.baidu.com/',
#     'http://image.baidu.com/',
#     'http://python-china.org/',
#     'http://python-china.org/node/about',
#     'http://python-china.org/node/',
#     'http://python-china.org/account/signin',
#     'http://python-china.org/account/signup',
#     'http://www.qq.com',
#     'http://www.youku.com',
#     'http://www.tudou.com'
# ]
#
# start = time.time()
# results = map(urllib.request.urlopen, urls)
# print('Normal:', time.time() - start)
#
# start2 = time.time()
# # 开8个 worker，没有参数时默认是 cpu 的核心数
# pool = ThreadPool(processes=4)
# # 在线程中执行 urllib2.urlopen(url) 并返回执行结果
# results2 = pool.map(urllib.request.urlopen, urls)
# pool.close()
# pool.join()
# print('Thread Pool:', time.time() - start2)

#!/bin/env python
#coding:utf-8
#coding:utf-8
# from concurrent import futures
# import urllib.request
#
# URLS = ['http://www.xiaorui.cc/',
#         'http://blog.xiaorui.cc/',
#         'http://ops.xiaorui.cc/',
#         'http://www.sohu.com/']
#
# def load_url(url, timeout):
#     print('收到任务{0}'.format(url))
#     return urllib.request.urlopen(url, timeout=timeout).read()
#
# with futures.ThreadPoolExecutor(max_workers=5) as executor:
#     future_to_url = dict((executor.submit(load_url, url, 60), url)
#                          for url in URLS)
#
#     for future in futures.as_completed(future_to_url):
#         url = future_to_url[future]
#         if future.exception() is not None:
#             print('%r generated an exception: %s' % (url,
#                                                      future.exception()))
#         else:
#             print('%r page is %d bytes' % (url, len(future.result())))

# import concurrent.futures
# import math
#
# PRIMES = [
#     112272535095293,
#     112582705942171,
#     112272535095293,
#     115280095190773,
#     115797848077099,
#     1099726899285419]
#
# def is_prime(n):
#     if n % 2 == 0:
#         return False
#
#     sqrt_n = int(math.floor(math.sqrt(n)))
#     for i in range(3, sqrt_n + 1, 2):
#         if n % i == 0:
#             return False
#     return True
#
# def main():
#     with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
#         for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
#             print('%d is prime: %s' % (number, prime))
#
# if __name__ == '__main__':
#     main()
import time
data=[x for x in range(1,1000000)]
from multiprocessing import Pool

def f(x):
    print(x*x)

if __name__ == '__main__':
    start_time=time.time()
    p = Pool(4)
    p.map(f,data)
    # p.close()
    # p.join()
    end_time=time.time()
    period=end_time-start_time
    print(type(period))
    print('耗时: ')
    print(period)