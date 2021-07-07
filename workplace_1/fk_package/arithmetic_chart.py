# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 12:20:10 2020

@author: Chenyang
"""

def print_arithmetic_chart(n):
    #打印乘法口诀表的函数
    for i in range(n):
        for j in range(i+1):
            print("%d * %d = %2d" % ((j+1),(i+1),(j+1)*(i+1)),end=" | ")
        print("")

if __name__ == "__main__":
    print_arithmetic_chart(5)