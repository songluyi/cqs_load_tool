# -*- coding: utf-8 -*-
# 2016/7/31 21:31
"""
-------------------------------------------------------------------------------
Function:
Version:    1.0
Author:     SLY
Contact:    slysly759@gmail.com 
 
-------------------------------------------------------------------------------
"""
from ftplib import FTP
ftp = FTP('ftp.debian.org')
print(ftp.login())