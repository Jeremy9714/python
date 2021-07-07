# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 10:54:22 2020

@author: Chenyang
简单的模块，该模块包含以下内容
my_list: 保存列表的变量
print_triangle: 打印由星号组成的三角形的函数
"""
my_list = ["Python", "Kotlin", "Swift"]
def print_triangle(n):
    if n <=0:
        raise ValueError("n必须大于零")
    for i in range(n):
        print(" " * (n-i-1),end = "")
        print("*" * (2*i+1),end = "")
        print("")
#测试代码
def test_print_triangle():
    print(print_triangle(3))
    print(print_triangle(4))
    print(print_triangle(7))
if __name__ == "__main__": test_print_triangle()