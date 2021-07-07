# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 11:42:47 2020

@author: Chenyang
测试__all__变量的模块
"""

def Ahello():
    print("hello world")
def Aworld():
    print("this is a funny world")
def Atest():
    print("test")
#__all__变量将模块变量的值设置成一个列表，只有该列表中的程序单元才会被暴露出来
__all__ = ["Ahello", "Aworld"]
