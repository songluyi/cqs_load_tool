# -*- coding: utf-8 -*-
# 2016/7/29 16:35
"""
-------------------------------------------------------------------------------
Function:
Version:    1.0
Author:     SLY
Contact:    slysly759@gmail.com 
 
-------------------------------------------------------------------------------
"""
from PyQt5 import QtWidgets
#从PyQt库导入QtWidget通用窗口类
class mywindow(QtWidgets.QWidget):
#自己建一个mywindows类，以class开头，mywindows是自己的类名，
#（QtWidgets.QWidget）是继承QtWidgets.QWidget类方法，
    def __init__(self):
        super(mywindow,self).__init__()

import sys
app = QtWidgets.QApplication(sys.argv)
windows = mywindow()
label=QtWidgets.QLabel(windows)     #在窗口中绑定label
label.setText("hello world")

windows.show()
sys.exit(app.exec_())