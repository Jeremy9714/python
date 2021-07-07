# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 10:21:39 2020

@author: Chenyang

该模块包含以下内容
my_book: 字符串变量
say_hi: 简单的函数
User: 代表用户的类
"""
print("this is module 1")
my_book = "讲义"
def say_hi(user):
    print("%s,欢迎学习python"%user)
#模块的测试函数
def test_my_book():
    print(my_book)
def test_say_hi():
    say_hi("孙悟空")
    say_hi(User("charlie"))
def test_User():
    u = User("白骨精")
    u.walk()
    print(u)
    
class User:
    def __init__(self,name):
        self.name = name
    def walk(self):
        print("%s is walking slowly"%self.name)
    def __repr__(self):
        return "User[username=%s]"%self.name
"""
如果直接使用python命令来来运行一个模块，__name__变量的值为__main__
如果该模块被导入其他程序中，__name__变量的值就是模块名
"""
if __name__ == "__main__": 
    test_my_book()
    test_say_hi()
    test_User()