# -*- coding: utf-8 -*-
# 2016/7/31 21:31
"""
-------------------------------------------------------------------------------
Function:   一键上传至FTP
Version:    1.0
Author:     SLY
Contact:    slysly759@gmail.com 
 
-------------------------------------------------------------------------------
"""
import paramiko
import os,time,shutil
from cqs_branch_connect_database import get_batch_id
def get_path():
    import os
    path=os.getcwd()
    FileList = []
    rootdir = path
    for root, subFolders, files in os.walk(rootdir):
        #排除特定的子目录
        if 'done' in subFolders:
            subFolders.remove('done')
        #查找特定扩展名的文件，只要包含'索引表'但不包含"new"字符串的文件，都会被包含
        for f in files:
            if f.find('表') != -1 and f.find('new')==-1:
                FileList.append(os.path.join(root, f))
    return FileList
today_time=time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
new_ftp_path=str(today_time)+' '+str(get_batch_id())
remotepath='/'+new_ftp_path+'/'
os.mkdir(new_ftp_path)
base_path=os.getcwd()
namelist=get_path()
for name in namelist:
    shutil.copy(name,new_ftp_path)
    print(name)
excel_path=base_path+'\\'+new_ftp_path
os.chdir(excel_path)
print(os.getcwd())
namelist=get_path()
count_index=1
count_rate=1
ftp=paramiko.Transport(('127.0.0.1', 22))
ftp.connect(username='admin', password='admin', hostkey=None)
sftp =paramiko.SFTPClient.from_transport(ftp)
sftp.mkdir(new_ftp_path)
print(sftp.listdir())
print(sftp.getcwd())
for name in namelist:
    if '索引表' in name:
        newname='cqs_index_'+str(count_index)+'.xlsx'
        count_index+=1
        os.rename(name,newname)
        remotepath_index=remotepath+newname
        sftp.put(newname,remotepath_index)
    if '等级表' in name:
        newname='cqs_rate_'+str(count_rate)+'.xlsx'
        count_rate+=1
        os.rename(name,newname)
        remotepath_rate=remotepath+newname
        sftp.put(newname,remotepath_rate)
print(sftp.listdir())
ftp.close()

