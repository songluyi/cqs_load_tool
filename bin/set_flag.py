# -*- coding: utf-8 -*-
# 2016/8/31 15:17
"""
-------------------------------------------------------------------------------
Function:
Version:    1.0
Author:     SLY
Contact:    slysly759@gmail.com 
 
-------------------------------------------------------------------------------
"""
import argparse
parser = argparse.ArgumentParser(description='choose new_load_data like zero or load_data like one.')
parser.add_argument('-t', action="store", dest="choice_value", type=int)
args = parser.parse_args()
print(type(args))
print(type(args.choice_value))
print(args.choice_value)