# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 21:25:23 2020

@author: Chenyang
"""
def Task1():
    #复数的虚部用j或者J来表示
    ac1 = 3 + 0.2j
    print(ac1,type(ac1))
    ac2 = 4 - 0.1j
    print(ac1+ac2)
    
    #cmath模块下的函数，用于计算平方根
    import cmath
    ac3 = cmath.sqrt(-1)
    print(ac3)
    
    str1 = "\"great\", says the boy"
    print(str1)
    str2 = "."
    str3 = "Hello ""world" #如果直接将两个字符串紧挨着写在一起，Python就会自动拼接它们
    print(str1+str2,'\n'+str3)
    

if __name__== '__main__':
    Task1()