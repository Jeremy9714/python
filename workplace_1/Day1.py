# -*- coding: utf-8 -*-
"""
Created on Fri May 29 21:01:49 2020

@author: Chenyang
"""
import keyword#查找关键字
import cmath#c代表complex
import time
import random
import enum

# =============================================================================
# Tab/Shift+Tab:代码缩进/撤销代码缩进
# Ctrl+1:注释/撤销注释
# Ctrl+4/5:块注释/撤销块注释
# Ctrl+L:跳转到行号
# F5:运行
# F11:全屏
# =============================================================================

def Task1():
    a = [1,2,3,4]
    for i in a:
        print(i)
    print(type(a))
# =============================================================================
# 
# =============================================================================
def Task2():
    #print(value...,sep=' ',end='\n',file=std.out,flush=False)
    print(keyword.kwlist)
    f= open("poem.txt","w")
    print("time","is","money",sep='  ',file = f)
    #不会出现溢出
    a=666666666666666666666
    print(a,type(a))
    a=None
    print(a,type(a))
    f.close()
# =============================================================================
#     
# =============================================================================
def Task3():#进制
    #以0x或0X开头的整数类型是十六进制形式的整数
    hex_value1 = 0x13
    hex_value2 = 0XaF
    print(hex_value1, hex_value2)
    #以0b或0B开头的整数类型是二进制形式的整数
    bin_value1 = 0b111
    bin_value2 = 0B101
    print(bin_value1,bin_value2)
    #以0o或0O开头的整数类型是八进制形式的整数
    oct_value = 0O11
    print(oct_value)
    #为了提高数值的可读性，允许为数值(包括浮点型)增加下划线作为分隔符
    one_million = 1_000_000
    one_billion = 1_000_000_000
    decimals = 1_000.12
    print(one_million,one_billion,decimals,sep='|')
# =============================================================================
# 
# =============================================================================
def Task4():#浮点型和复数
    #浮点型
    af1 = 5.2345556
    print(af1,type(af1))
    #科学计数形式(浮点型)
    f1 = 5.12e2
    f2 = 5e3
    print(f1, type(f1),f2, type(f2),sep='|')
    #复数的虚部用j或J来表示
    ac1 = 3 + 0.2j
    print(ac1,type(ac1))
    ac2 = cmath.sqrt(-1)
    print(ac2,type(ac2))
# =============================================================================
#     
# =============================================================================
def Task5():#字符串
    str1 = "jeremy is a \"monster\" "
    print(str1)
    str2 = "said the president"
    print(str1+str2)
    #如果两个字符串紧挨在一起，则会被自动拼接
    str3 = "Hello " "world"
    print(str3)
    #str()和repr()
    s1 = "price: "
    p = 231
    print(s1+str(p),s1+repr(p),sep='|')
    s2 = "this is a sentence"
    print(str(s2),repr(s2),sep='|')#repr()会以python表达式的形式来表示值
    #输入值
    msg = input("please input a number:")
    print(msg,type(msg))#input()返回值类型为str
    #长字符串
    s = '''213"sfdfsd''dsfs"'"'''
    print(s)
    #转义字符'\'可以将换行符进行转义，可以将字符串分成两行
    s2 = "this is a very long \
    sentence"
    print(s2)
    #原始字符串
    s1 = r"D:\desktop\scripts\python\day1"#原始字符串以'r'开头，原始字符串不会把反斜线当成特殊字符
    print(s1)
    s2 = r"jeremy is a \"monster\""#原始字符串中的引号同样需要进行转义，但用于转移的反斜线会变成字符串的一部分
    print(s2)
    #字节串
    b1 = b"hello"#通过直接在字符串前面添加b来构建字节船值
    print(b1,b1[2],b1[2:4])
    b2 = bytes("这是一句中文",encoding = 'utf-8')#调用bytes()方法将字符串按指定字符集转换成字节串
    print(b2)#十六进制数
    b3 = "这是另一句中文".encode('utf-8')#调用字符串本身的encode()方法将字符串按指定的字符集转换成字节串
    print(b3)
    st = b3.decode('utf-8')#decode()方法将bytes对象解码成字符串
    print(st)
# =============================================================================
# 
# =============================================================================
def Task6():
    #字符串格式化
    price = 108
    print("the price for an apple is %s" %price)
    user = "Jeremy"
    age = 23
    print("%s is %s years old" %(user, age))
    
    #转换说明符
    print("num is %i" %price)#转换为带符号的十进制形式的整数
    print("num is %6d" %price)
    print("num is %6o" %price)#转换为带符号的八进制形式的整数
    print("num is %6x" %price)#转换为带符号的十六进制形式的整数
    print("num is %6X" %price)
    print("nun is %6e" %price)#转换为科学计数法表示的浮点数
    print("num is %6f" %price)#转换为十进制形式的浮点数
    print("num is %6g" %price)#智能选择使用e或f格式
    print("num is %6s" %price)#使用str()将变量或表达式转换为字符串
    print("num is %6r" %price)#使用repr()将变量或表达式转换为字符串
    print("num is %6c" %price)#转换为单字符(只接受整数或单字符字符串)
    #数字表示转换后的最小宽度(默认情况字符串总是右对齐)
    num2 = 30
    print("num2 is: %06d" %num2)#0表示不补充空格，而是补充0
    print("num2 is: %+6d" %num2)#+表示数值总要带着符号
    print("num2 is: %-6d" %num2)#-表示左对齐
    
    #指定数字位数
    temp = 3.141592656
    print("my_value is %6.3f" %temp)#精度值放在最小宽度后面，中间用'.'隔开
    temp2 = "Jeremy"
    print("my name is %.2s" %temp2)#只保留2个字符
    
    #大小写相关方法
    print(dir(str))#列出指定类或模块包含的全部方法
    print(help(str.title))#查看某个函数或方法的帮助文档
    a = "our domain is crazyit.org"
    print(a.title())#将每个单词的首字母改为大写
    print(a.lower())#将整个字符串改为小写
    print(a.upper())#将整个字符串改为大写
    
    #删除空白
    s = "    this is a sentence  "
    print(s.strip(),'.',sep='|')#删除字符串前后的空格
    print(s.lstrip(),'.',sep='|')#删除字符串左边的空格
    print(s.rstrip(),'.',sep='|')#删除字符串右边的空格
    s = "this is another sentence"
    
    #删除字符串前后指定字符
    print(s.lstrip("thus"))
    print(s.rstrip("sence"))
    
    #查找、替换
    s = "crazyit.org is a terrible site"
    print(s.startswith("crazyit"),s.endswith("site"))#判断字符串是否以指定字串开头‘结尾
    print(s.find("terrible"))#返回字符串中子串出现的位置，若不存在则返回-1
    print(s.index("terrible"))#查找子串在字符串中出现的位置，若不存在，则引发ValueError错误
    #print(help(str.find),help(str.index),sep='\n')
    print(s.find("it",11))#在字符串[start,end)区间查找子串出现位置
    #print(help(str.replace))
    print(s.replace("it","its",1))
    print(s.replace("it","its"))
    #print(help(str.translate))
    table = {97:945,98:946,116:964}
    print(s.translate(table))#使用指定映射表对字符串进行替换
    table = str.maketrans("a","1")#第一个参数为被替换的字符，第二个参数为被替换的字符
    print(table)#储存为unicode码
# =============================================================================
#     
# =============================================================================
def Task7():
    #分割和连接方法
    #print(help(str.split))
    #print(help(str.join))
    s = "my homepage is chenyang.com"
    print(s.split('.'))
    mylist = s.split(None,2)
    print('|'.join(mylist))#'|'作为分隔符，将mylist连接成字符串
    #乘法运算符
    print("this "*5)
    
    #比较运算符
    a = time.gmtime()
    b = time.gmtime()
    print(a==b)
    print(a is b)#判断两个变量是否指向同一个对象
    print(id(a),id(b))#id()返回变量所引用对象的内存地址
    
    #三目运算符
    a = input("enter a number:")
    b = input("enter another number:")
    print("1st try") if int(a)>int(b) else(print("2nd try") if int(a)*2>int(b) else print("failure"))
# =============================================================================
#     
# =============================================================================
def Chapter3_1():#列表、元组和字典
    my_list = [12,"jeremy",True]
    print(my_list)
    my_tuple = (12, "jeremy", None)#元组的元素不能修改
    print(my_tuple)
    
    #子序列
    a = [1,2,3,4,5,6,7,8,9,10]
    #切片[start: end: step] step为步长(间隔)
    print(a[2::2])
    
    #运算
    print(a+[11,12,13,14])
    #当元组执行加法或乘法运算时，若该元组只有一个元素，则需要在元素后面加','
    order_endings = ("st","nd","rd")\
    +("th",)*17 + ("st","nd","rd")\
    +("th",)*7 + ("st",)
    print(order_endings)
    day = input("enter a date(1-31):")
    print(day+order_endings[int(day)-1])
    
    #序列封包和序列解包
    #把多个值赋给一个变量时，会自动将多个值封装成元组
    vals = 1,2,3
    print(vals)
    a_tuple = tuple(range(1,10,2))#range(start, end, step)
    #程序允许将序列直接赋值给多个变量，此时序列的各元素会被依次赋值给每个变量
    a,b,c,d,e = a_tuple
    print(a,b,c,d,e,sep=',')
    #序列解包时也可以只解出部分变量。Python允许在左边被复制的变量前添加'*'，那么该变量就代表一个列表
    first, second, *third = range(10)
    print(third)
    
    #增加列表元素
    a = [1,2,3,4,5]
    a.append([6,7])#append()将传入的参数当成单个元素，追加到列表的最后面
    print(a)
    a.extend(range(1,10,2))#extend()追加列表中的元素
    print(a)
    a.insert(3,('d','e'))#insert()将元素插入到指定位置
    print(a)
    
    #删除列表元素
    del a[::2]#del语句可以删除列表中的某个元素，也可以直接删除列表的中间一段
    print(a)
    #del a#同时也可以删除普通变量
    #print(a)
    a.remove(5)#remove(val)方法删除找到的第一个val
    print(a)
    
    #修改列表元素
    a[2:2] = ['x','xx']#对列表中空的slice赋值，就变成了向列表插入元素
    print(a)
    a[2:6] = []#将列表一段赋值为空列表，就变成了从列表中删除元素
    print(a)
    a[1:3] = "jeremy"#对列表使用silce语法赋值时，不能使用单个值；如果使用字符串赋值，Python会自动把字符串当成序列处理
    print(a)
# =============================================================================
# 
# =============================================================================
def Chapter3_2():
    #列表的其他常用方法
    a = list(range(10))
    print(a.count(1))
    print(a.index(9))
    stack = []
    for i in range(1,5):
        stack.append(i)
    print(stack)
    print(stack.pop())#最后入栈的元素被移除
    print(stack)
    
    #字典
    dic1 = {(1,2):2,3:4}
    print(type(dic1), dic1)#字典的key值必须是不可变类型
    dic2 = dict([[1,'a'],[2,'b'],[3,'c']])
    print(dic2)
    dic3 = dict(a = 1.3, b = 1.4)#使用关键字参数创建字典，字典的key值不允许使用表达式
    print(dic3)
    
    #字典的常用方法
    dic = dict(a=1,b=2,c=3,d=4,e=5)
    print(dic.get('b'))#get()方法根据key值来获取value;如果key不存在，则返回None
    dic.update({'a':10,'f':6})#update()方法覆盖字典中已包含的key-value对的value值；若key不存在，则该key-value对被添加进去
    print(dic)
    ims = dic.items()#items()方法获取字典中所有的key-value对，返回一个dict_items对象
    print(list(ims))
    kys = dic.keys()#keys()方法获取字典中所有的key,返回一个dict_keys对象
    print(list(kys)[2])
    ves = dic.values()#values()方法获取字典中所有的value,返回一个dict_values对象
    print(list(ves)[2])
    print(dic.pop('a'))#pop()方法用于获取指定key对应的value,并删除这个key-value对
    print(dic.popitem())#popitem()方法弹出字典底层储存最后一个key-value对
    k,v = dic.popitem()
    print(k,v)
    '''
    setdefault()方法用于根据key值来获取对应的value;若key不存在，则可该方法会先对这个不
    存在的key设置一个value
    '''
    print(dic.setdefault('e',5))
    print(dic)
    print(dict.fromkeys(['f','g','h'],6))#fromkeys()方法用于给给定的多个key创建字典，这些key对应的value默认值为None;也可以额外传入一个参数作为默认value
    
    #使用字典格式化字符串
    #在字符串模板中使用key
    temp = "书名是：%(name)s, 价格是: %(price)010.2f, 出版社是: %(publisher)s"
    books = dict(name = "english", price = 12.766, publisher = "UK")
    print(temp %books)
# =============================================================================
# 
# =============================================================================
def Chapter4_1():#流程控制
    #if分支结构
    print("helloWorld") if random.randint(0,9)>3 else print("Unwelcomed")
    pass#空语句
    #断言
    age = input("输入年龄:")
    #assert语句用于对一个bool表达式进行断言，如果表达式为True,则继续向下执行；否则引发AssertionError错误
    assert 18<int(age)<60
    print("无法退休")
    
    #for-in循环
    A = [12, 34, "jeremy ", 1.02, 'is a genius']
    text = ""
    result = 0
    for a in A:
        #isinstance(obj, type)函数判断变量是否为某个类型的实例
        if isinstance(a, int) or isinstance(a, float):
            result+=a
        else:
            text+=a
    print(result, text)
    #遍历列表或元组
    b = (12,"we",1.2,'x')
    for i in range(len(b)):
        print("第%d个元素是 %s"%(i,b[i]))
    #遍历字典
    c = dict(a=12,b=22,c=32,d=42,e=52)
    for key, value in c.items():
        print("key:",key,"value:",value)
        
    #统计元素出现次数
    d = [12,5,'a',3.2,'a',"jeremy",2,3.66,'c',5]
    result = dict()
    for i in d:
        if i in result:
            result[i]+=1
        else:
            result[i]=1
    for key, value in result.items():
        print("%s出现的次数为: %d"%(key, value))
    #循环使用else
    for i in d:
        print(i)
    else:#for循环可以使用else块
        print(i)
        
    #for表达式
    a_list = [x for x in range(10)]
    print(a_list)
    b_list = [(x,y) for x in range(4) for y in range(5)]
    print(b_list)
    
    #常用工具函数
    print([x for x in zip(a_list,b_list)])#zip()函数将两个列表压缩成一个zip对象；若两个列表长度不同，则zip()函数将以更短的列表为准
    a = [1,2,3]
    b = ['a','b','c']
    for num, alpha in zip(a,b):
        print(num,alpha)
    c = ['a','bb','ccc','dd','e']
    print(sorted(c,reverse = True,key=len))#sorted()函数可以传入一个key参数，用于指定一个函数来生成排序的关键值
# =============================================================================
# 
# =============================================================================
def Chapter4_2():#习题
    pass
# =============================================================================
# 
# =============================================================================
def Max(x,y):
    '''
    该函数的说明文档
    '''
    z = x if x>y else y
    return z

def girth(width, height):
    print("width: %d height: %d" %(width, height))
    return 2*(width+height)

def test1(var1 = 0, var2 = 1, var3 = 2):#参数默认值
    return sum((var1, var2, var3))

def test2(name="default_name", message = "default_msg"):
    print(name, message)

def test3(a, *books):#在星餐前面添加一个星号，就意味着调用函数时可以传入任意多个参数，多个参数值被当成元组传入
    print(a, books, len(books), sep='\n')

def test4(x,y,z=3,*books,**scores):#**用来收集关键字参数(字典)
    print(x,y,z)
    print(books)
    print(scores)

def test5(name, message):#逆向参数收集；将已有列表、元组、字典的元素拆开传给函数的参数
    print(name, message)

def test6(book, price, desc):
    print("book", book, "worth", price)
    print("desc:", desc)
    
def Chapter5_1():#函数
    #函数的说明文档
    print(help(Max))
    print(Max.__doc__)#通过函数的__doc__属性访问函数的说明文档
    print(girth(10, height= 12))#使用关键字参数来传入参数值(必须将位置参数放在关键字参数之前)
    print(girth(height=10, width = 12))#使用关键字参数时可交换位置
    print(test1(10,11))
    print(test1(12,var3=12))#指定参数使用默认值
    #python要求将带默认值的参数定义在形参列表的最后
    #test2("nice_msg",name="nice_name")
    
    #参数收集
    test3(12,1,2,3)
    test4(1,2,3,"history","grammer",Math = 'A', Art = 'B')
    #逆向参数收集
    my_list = ["aa", "bb"]
    test5(*my_list)#逆向参数收集需要在传入的列表、元组参数之前添加一个星号，在字典参数前添加两个星号
    my_dict = dict(price = 12, book = "HelloWorld", desc = "nothing")
    test6(**my_dict)#字典也支持逆向手机，字典将会以关键字的形式传入
# =============================================================================
# 
# =============================================================================
def test7():
    age = 20
    print(age)
    print(locals())#locals()返回当前局部范围内所有变量组成的变量字典
    print(locals()['age'])
    locals()['age'] = 21#无法通过locals()修改局部变量的值(可以修改全局变量的值)
    print(age)
    print(globals()['X_X'])#globals()返回全局范围内的所有变量组成的字典
    globals()['X_X'] = 21#可以通过globals()修改全局变量
    print(X_X)
X_X = 12
#locals()['X_X'] = 100#locals()可以修改全局变量
#print(X_X)

def test8():
    global X_X#声明变量为全局变量，后面的赋值语句不会重新定义局部变量
    print(X_X)
    X_X = 'X_X'#全局变量

def get_math_func(op, num):#局部函数只能在其封闭函数内有效
    def square(n):
        return pow(n,2)
    def cube(n):
        return pow(n,3)
    def factorial(n):
        result = 1
        for i in range(1,n+1):
            result*=i
        return result
    if op=="square":
        return square(num)
    elif op=="cube":
        return cube(num)
    elif op=="factorial":
        return factorial(num)
    else:
        print("wrong input")

def foo():
    name = "jeremy"#局部变量
    def bar():
        nonlocal name#nonlocal语句声明访问赋值语句只是访问该函数所在函数内的局部变量
        print(name)#局部变量
        name = "jezza"
    bar()

def Chapter5_2():
    #变量作用域
    test7()
    print()
    test8()
    print(X_X)   
    
    #局部函数
    print(get_math_func("cube",5))
    print(get_math_func("subtraction",3))
    foo()
    
    #函数的高级内容
    #使用函数变量
    print(type(foo))#所有函数都是function对象
    def pow(base, exponent):
        result = 1
        for i in range(1,exponent+1):
            result*=base
        return result
    func_1 = pow#将pow函数赋值给变量
    print(func_1(2,3))
    def area(width, height):
        return width*height
    func_1 = area#可以让变量在不同的时间指向不同的变量
    print(func_1(3,4))
    
    #使用函数作为函数形参
    def map(iterable, fn):#动态传入函数
        """
        my_func_map
        """
        result = []
        for e in iterable:
            result.append(fn(e))
        return result
    def square(n):
        return n*n
    def cube(n):
        return pow(n,3)
    data = [1,2,3,4,5]
    print(map(data,square))#第二个参数为函数参数
    print(map(data,cube))
    print(map.__doc__,type(map))
    
    #函数作为返回值
    def math_func(fn):
        def square(n):
            return n*n
        def cube(n):
            return pow(n,3)
        if fn=="square":
            return square#使用局部函数作为返回值
        else:
            return cube
    math_func1 = math_func("square")#返回一个嵌套函数(square函数)
    print(math_func1(2))
    
    #局部函数与lambda表达式
    #使用lambda表达式代替局部函数
    def math_func(fn):
        if fn=="square":
            return lambda n:n*n
        elif fn=="cube":
            return lambda n:n*n*n
        else:
            return lambda n:(n+1)*n/2
    math_func1 = math_func("square")
    math_func2 = math_func("other") 
    print(math_func1(2))
    print(math_func2(2))
    
    #lambda表达式语法: lambda[parameter_list]: expression
    def map(fn,data):
        result = []
        for i in data:
            result.append(fn(i))
        return result
    x = map(lambda n:n*n, range(1,8))
    print([e for e in x])
    x = map(lambda n:n*n if n%2==0 else 0, range(1,8))#lambda表达式只能创建简单的函数对象(函数体为单行)
    print([e for e in x])
# =============================================================================
# 
# =============================================================================
class Person:
    hair = "black"#类变量
    #实例方法的第一个参数self表示方法的调用者
    def __init__(self,name = "Jeremy",age = 8):#构造函数
        self.name = name
        self.age = age
    def say(self,content):
        print(content)
    def output(self):
        print(self.name, self.age)

def Chapter6_1():#类和对象
    p = Person()#调用类的构造方法，返回一个类对象
    p.say("this is a sentence")
    p.output()
    
    #对象的动态性
    p.skills = [1,2]
    print(p.skills)#可以给对象添加实例变量
    del Person.hair
    #print(p.hair)
    
    #动态增加方法
    def info(self):
        print("info函数", self)
    p.foo = info#动态增加方法
    #python不会将动态增加的方法的调用者绑定到它们的第一个参数
    p.foo(p)#手动绑定调用者
    p.bar = lambda self:print("lambda",self)
    p.bar(p)
    
    def intro_func(self,content):
        print("infomation is that %s" % content)
    #通过MethodType()对动态增加的方法进行包装，将函数的第一个参数绑定为调用对象
    from types import MethodType
    p.intro = MethodType(intro_func,p)
    p.intro("HelloWorld")#无需传入调用者
# =============================================================================
# 
# =============================================================================
class Dog:
    def jump(self):
        print("jump")
    def run(self):
        self.jump()
        print("run")

class User:
    def test(self):
        print("self",self)

class ReturnSelf:
    def grow(self):
        if hasattr(self,"age"):
            self.age+=1
        else:
            self.age = 1
        return self#返回调用该方法的对象(C++引用)

class Bird:
    def foo():
        print("foo")
    bar = 20#类变量
    def foobar(self):#实例方法
        print(self, "is the caller")

class Bar:
    @classmethod#修饰的方法是类方法
    def fly(cls):#类函数要求第一个参数cls表示类
        print("类方法",cls)
    @staticmethod#修饰的方法是静态方法
    def info():
        print("静态方法")

def Chapter6_2():
    d = Dog()
    d.run()
    
    #自动绑定的self参数并不依赖具体调用方式
    u = User()
    u.test()#方法调用
    foo = u.test
    foo()#变量(函数形式)调用
    rs = ReturnSelf()
    rs.grow().grow().grow()#self可以作为返回值，则可以多次连续调用方法
    print(rs.age)
    
    #方法
    #类调用实例方法
    Bird.foo()
    print(Bird.bar)
    #Bird.foobar()#类调用实例方法时不会自动为第一个参数绑定调用者
    Bird.foobar("hello")#实用类调用实例方法时可以显式地为第一个参数self传入调用者(称为未绑定方法)
    
    #类方法和静态方法
    Bar.fly()#调用类方法，类会自动绑定到第一个参数
    Bar.info()#调用静态方法，不会自动绑定
    b = Bar()
    b.fly()#使用对象也可以调用类方法
    b.info()
    
    #函数装饰器@
    #当使用@函数锈蚀另一个函数时：
    #1)将被修饰的函数作为参数传给@符号引用的函数
    #2)将被修饰的函数替换成第一步的返回值
    def funA(fn):
        print("A")
        fn()
        return "fkit"
    @funA
    def funB():
        print("B")
    print(funB)
    
    #将被锈蚀函数变为另一个函数
    def outer(fn):
        def inner(*args):
            print("1)",args)
            n = args[0]
            print("2)",n*(n-1))
            print(fn.__name__)#返回模块的名字
            fn(n*(n-1))
            print('*'*15)
            return fn(n*(n-1))
        return inner
    @outer
    def my_test(name):
        print("my_test函数名",name)
    my_test(10)#my_test函数变为inner函数
    my_test(6,5)
    print()
    
    #为函数添加功能
    def auth(fn):
        def auth_fn(*args):
            print("processing authorization")
            fn(*args)#回调被修饰的函数
        return auth_fn
    @auth
    def test(a,b):
        print("执行test函数, 参数a:%s, 参数b:%s"%(a,b))
    test(20,15)
# =============================================================================
# 
# =============================================================================
class Category:
    cate_fn = lambda p: print("该lambda表达式的值为:",p)#实例方法
    @classmethod
    def fn(cls):
        print("classmethod")

class Inventory:
    item = "mouse"
    quantity = 100
    def change(self, item, quantity):
        #通过对象对类变量赋值，不是对类变量赋值，而是定义新的实例变量
        self.item = item
        self.quantity = quantity

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def setSize(self, size):
        self.width, self.height = size
    def getSize(self):
        return self.width, self.height
    def delSize(self):
        self.width, self.height = 0, 0
    Size = property(getSize, setSize, delSize, "用于描述矩形大小的属性")

class Cell:
    @property
    def state(self):
        return self._state
    @state.setter
    def state(self,val):
        if "alive" in val.lower():
            self._state = "alive"
        else:
            self._state = "dead"
    @property
    def is_dead(self):
        return not self._state.lower() == "alive"
      
class Goods:
    def __init__(self):
        self.age =12
    @property
    def price(self):
        return self.age
    @price.setter
    def price(self,val):
        self.age = val
    @price.deleter
    def price(self):
        self.age = 0
        
def Chapter6_3():
    #全局空间和类命名空间分别定义lambda表达式
    global_fn = lambda p: print("该lambda表达式的值为:",p)
    global_fn("value")
    c = Category()
    c.cate_fn()
    Category.fn()
    
    #成员变量
    iv = Inventory()
    iv.change("keyborad",1000)
    print(iv.item,iv.quantity)
    print(Inventory.item,Inventory.quantity)
    
    #使用property函数定义属性: property(fset=None, fget=None, fdel=None, doc=None)
    #property()函数可以将类的方法定义成属性(相当于实例变量)
    print(Rectangle.Size.__doc__)#访问文档说明
    print(help(Rectangle.Size))#通过内置的help()函数访问说明文档
    rect = Rectangle(2,5)
    print(rect.Size)
    rect.Size = 5,6#对属性赋值
    print(rect.width,rect.height)
    del rect.Size
    print(rect.width,rect.height)
    
    #使用装饰器来修饰方法
    c = Cell()
    c.state = "alive"
    print(c.state)
    print(c.is_dead)
    
    g = Goods()
    print(g.price)
    g.price = 100
    print(g.price)
    del g.price
    print(g.price)
# =============================================================================
# 
# =============================================================================
class Student:
    def __hide(self):#以"__"开头的类的成员会被隐藏起来
        print("隐藏的方法hide")
    def get_name(self):
        return self.__name
    def set_name(self,name):
        if len(name)<3 or len(name)>8:
            raise ValueError("用户名长度必须在3~8之间")
        self.__name = name
    name = property(get_name, set_name)
    def get_age(self):
        return self.__age
    def set_age(self, age):
        if age < 18 or age > 60:
            raise ValueError("用户名年龄必须在18~60之间")
        self.__age = age
    age = property(get_age, set_age)

class Fruit:
    def info(self):
        print("weight is: %d"%self.weight)
class Food:
    def taste(self):
        print("sweet")
    def info(self):
        print("Food info")
#class Sub_class(Super_class_1, Super_class_2...)
class Apple(Food,Fruit): #当多个父类中包含了同名方法，排在前面的父类方法会遮蔽排在后面的父类方法
    pass

class Base_class:
    def foo(self):
        print("Base_class foo")
        
class Derived_class(Base_class):
    def foo(self):
        print("Derived_class")
    def bar(self):
        print("bar")
        self.foo()
        Base_class.foo(self) #使用类名调用实例方法调用父类被重写的方法

class Employee:
    def __init__(self,salary):
        self.salary = salary
    def work(self):
        print("salary is %d"%self.salary)
        
class Customer:
    def __init__(self, favorite, address):
        self.favorite = favorite
        self.address = address
    def info(self):
        print("我是一个顾客，爱好是%s, 地址是%s"%(self.favorite, self.address))
        
class Manager(Employee, Customer):
    def __init__(self,salary, favorite, address):
        print("Manager constroctor")
        #通过1super对象既可调用父类的实例方法，也可调用父类的类方法
        super().__init__(salary)
        #super(Manager,self).__init__(salary) #super(class_type, obj)同上
        Customer.__init__(self,favorite, address) #使用未绑定方法调用父类的构造方法

class Cat:
    def __init__(self, name):
        self.name = name    
def walk_func(self):
    print("%s is walking through a piece of lawn"%self.name)

class Puppy:
    #__slots__属性的值是一个元祖，该元组的所有元素列出了该类的实例允许动态添加的所有属性名和方法名
    __slots__ = ("run","name","age")
    def __init__(self,name):
        self.name = name
    def test():
        print("test方法")

class Wolf_Puppy(Puppy):
    __slots__ = ("speed", "colour")
    def __init__(self,name):
        super().__init__(name)
        pass
        
def Chapter6_4():
    #隐藏和封装
    #python会将以双下划线开头命名的python类的成员隐藏起来
    s = Student()
    s.name = "jeremy"
    s.age = 23
    print(s.name, s.age)
    #python并没有真正的隐藏机制，python会在这些方法名前添加单下划线和类名
    s._Student__hide()
    s._Student__name = 30 #绕开setter方法的检查逻辑，对隐藏变量进行赋值
    print(s.name)
   
    #类的继承
    #子类的方法会覆盖父类的同名方法
    a = Apple()
    a.weight = 10
    a.info()
    a.taste()
    dc = Derived_class()
    dc.bar()
    
    #调用父类的构造方法
    #1) 使用未绑定方法
    #2) 使用super()函数调用父类方法
    #print(help(super))
    m = Manager(200,"tennis", "LN6 7DB")
    m.work()
    m.info()
    
    #python的动态性
    from types import MethodType
    c = Cat("Kitty")
    Cat.walk = walk_func #为类动态添加方法，该方法的第一个参数会自动绑定
    #c.walk = MethodType(walk_func, c)
    #Cat.walk = MethodType(walk_func, Cat)
    c.walk()
    
    #__slots__属性
    p = Puppy("Tom")
    #Puppy.run = lambda self: print("%s is running"%self.name) #为类动态添加方法
    p.run = MethodType(lambda self: print("%s is running"%self.name),p)
    p.run()
    #程序只允许为实例动态添加名字在__slots__元组中的属性或方法
    p.age = 100
    print(p.age)
    #__slots__属性不限制通过类来动态添加属性或方法
    Puppy.walk = walk_func
    p.walk()
    """
    __slots__属性的限制只针对当前类的实例起作用，对派生类不起作用
    #在派生类中定义__slots__属性，子类的实例允许动态添加的属性和方法
    就是父类的__slots__元组加上派生类的__slots__元组的和
    """
    wp = Wolf_Puppy("Jerry")
    wp.speed = 100
    print(wp.speed)
# =============================================================================
# 
# =============================================================================
class ItemMetaClass(type):
    #cls代表被动态修改的类
    #name代表被动态修改的类名
    #bases代表被动态修改的类的所有父类
    #attrs代表被动态修改的类的所有属性、方法组成的字典
    def __new__(cls, name, bases, attrs):
        attrs["cal_price"] = lambda self: self.price * self._discount
        return type.__new__(cls,name,bases,attrs)

#metaclass中的__new__方法会为目标类动态添加方法
class Book(metaclass=ItemMetaClass):
    __slots__ = ("name", "price", "_discount")
    def __init__(self,name, price):
        self.name = name
        self.price = price
    @property
    def discount(self):
        return self._discount
    @discount.setter
    def discount(self, discount):
        self._discount = discount

class CellPhone(metaclass=ItemMetaClass):
    __slots__ = ("price", "_discount")
    def __init__(self, price):
        self.price = price
    @property
    def discount(self):
        return self._discount
    @discount.setter
    def discount(self,discount):
        self._discount = discount

class Canvas:
    def __init__(self,name):
        self.name = name
    def draw_pic(self, shape):
        print("开始绘图")
        shape.draw(self.name)

class Triangle:
    def draw(self, canvas):
        print("在%s上绘制三角形"%canvas)
        
class Circle:
    def draw(self, canvas):
        print("在%s上绘制圆形"%canvas)

class A:
    pass
class B:
    pass
class C(A,B):
    pass
class D(A):
    pass

class Orientation(enum.Enum): #继承Enum类来派生枚举类
    #为枚举指定value
    EAST = '东'
    SOUTH = '南'
    WEST = '西'
    NORTH = '北'
    def info(self):
        print("this enumeration represents %s"%self.value)

class Gender(enum.Enum): #枚举类的构造器
    MALE = "男","阳刚"
    FEMALE = '女',"阴柔"
    def __init__(self,cn_name, desc):
        self._cn_name = cn_name
        self._desc = desc
    @property
    def desc(self):
        return self._desc
    @property
    def cn_name(self):
        return self._cn_name
    
def Chapter6_5():
    #使用type()函数定义类
    print(isinstance(Puppy, type)) #class是type的实例
    def fn(self):
        print("fn函数")
    """
    type()定义类时可指定三个参数
    参数一：创建的类名
    参数二：该类继承的父类集合(用元组表示)
    参数三：该字典对象为该类绑定的类变量和方法。其中key值是类变量和方法名，value值是普通值或者函数
    """
    Dog = type("Dog",(object,),dict(name="Jesse",info=lambda self: print("name is %s"%self.name)))
    d = Dog()
    print(d.name)
    d.info()
    Dog.walk = walk_func
    d.walk()
    
    #使用metaclass可以动态修改程序中的一批类，对他们集中进行某种修改
    #指定了metaclass的类在被创建时，metaclass的__new__方法就会被调用
    b = Book("PC World", 20)
    b.discount = 0.7 #调用setter方法
    print(b.cal_price()) #__new__方法动态添加了cal_price方法
    cp = CellPhone(20)
    cp.discount = 0.6
    print(cp.cal_price())
    
    #多态
    c = Canvas("画布一")
    #程序为方法传入的参数对象只需要具有指定方法就行，至于方法的行为特征，则完全取决于对象本身
    c.draw_pic(Triangle())
    c.draw_pic(Circle())
    
    #检查类型
    #issubclass(cls, class_or_tuple) 检查cls是否为后一个类或元组包含的多个类中任意类的子类
    #isinstance(obj, class_or_tuple) 检查obj是否为后一个类或元组包含的多个类中任意类的对象
    print(isinstance("abc",str))
    print(isinstance(str,object))
    print(isinstance("abc",(str,tuple,list)))
    print(issubclass(str, object))
    print(issubclass(str,list))
    print(issubclass(str,(list,tuple,object)))
    #python为所有类都提供了一个__bases__属性，可以查看该类的所有直接父类，返回一个元组
    print(C.__bases__)
    #python为所有类都提供了一个__subclasses__()方法，可以查看该类的所有直直接子类，返回一个列表
    print(A.__subclasses__())
    
    #枚举类
    #使用Enum()函数来创建枚举类，第一个参数是枚举类的类名，第二个参数是一个元组
    Season = enum.Enum("Season",("SPRING","SUMMER","AUTUMN","WINTER"))
    print(Season.SPRING) #枚举
    #每个枚举都有name(变量名)、value(枚举值的序号，通常从1开始)两个属性
    print(Season.SPRING.name) 
    print(Season.SPRING.value)
    print(Season(2)) #使用枚举值访问枚举对象
    print(Season["WINTER"]) #使用枚举变量名访问枚举对象
    #__members__属性返回一个字点，字典包含了枚举的所有实例
    for name, member in Season.__members__.items():
        print(name,"->",member,",",member.value)
    
    #通过继承Enum类来派生枚举类
    print(Orientation.SOUTH.value)
    print(Orientation['WEST'])
    print(Orientation('北'))
    Orientation.EAST.info() #枚举类额外定义方法
    for name, member in Orientation.__members__.items():
        print(name, "->",member,",",member.value)
    
    #枚举的构造器
    print("FEMALE的枚举名: %s, 枚举值: %s"%(Gender.FEMALE.name,Gender.FEMALE.value))
    #参数的构造器需要几个参数，枚举对象的value就必须指定几个值
    print(Gender.FEMALE.cn_name,Gender.FEMALE.desc)
# =============================================================================
#   
# =============================================================================
def Chapter7_1(): #异常处理
    """
    python的异常机制主要依赖try、except、else、finally和raise五个关键字
    1)try后缩进的代码块简称try块，里面放置的是可能引发异常的代码
    2)except后对应的是异常类型和一个代码块，用于表明该except块处理的代码块类型
    3)else块用于处理无异常出现时的情况
    4)finally块放在最后，用于回收在try块中打开的物理资源，异常机制会保证finally块总被执行
    5)raise可以单独作为语句使用，用于引发一个具体的异常对象
    python所有的异常类的基类是BaseException.BaseException的主要子类是exception类
    """
    import sys
    try:
        #sys木块的argv列表用来获取运行python程序时提供的参数
        a = int(sys.argv[1]) 
        b = int(sys.argv[2])
        c = a/b
        print("c is",c)
    except IndexError:
        print("输入的参数个数不够")
    except ValueError:
        print("程序只能接收整数参数")
    #except (IndexError, ValueError): #多异常捕获
    except ArithmeticError:
        print("算数错误")
    except Exception:
        print("未知错误")
    except:
        print("捕获所有类型的异常")
    
    def foo():
        try:
            fis = open("a.txt")
        #通过为异常对象声明变量来获得异常对象的相关信息
        except Exception as e:
            print(e.args) #args属性返回异常的错误编号和描述字符串
            print(e.errno) #errno属性返回异常的错误编号
            print(e.strerror) #strerror属性返回异常的描述字符串
            #print(e.with_traceback) #通过该方法可处理异常的传播轨迹信息
        else:
            print("没有出现异常")
            fis.close()
    foo()
    
    #else块
    s = int(input("请输入除数:"))
    try:
        result = 20/s
        print("20除以%s的结果为: %g"%(s,result))
    except ValueError:
        print("必须输入整数")
    except ZeroDivisionError as zde:
        print("0不能作为除数")
        print(zde)
    else:
        print("没有出现异常")
    
    def else_test():
        s = input("请输入除数:")
        result = 20/int(s)
        print("20除以%s的结果为: %g"%(s,result))
    def right_main():
        try:
            print("\ntry块代码无异常")
        except:
            print("程序出现异常")
        else:
            else_test() #else块中的异常不会被前面的except捕获
    def wrong_main():
        try:
            print("try块代码无异常")
            else_test()
        except:
            print("程序出现异常")
    wrong_main()
    right_main()
# =============================================================================
# 
# =============================================================================
def Chapter7_2():
    #finally回收资源
    #python的垃圾回收机制不会回收任何物理资源，只能回收堆内存中对象所占用的内存
    #import os
    def test():
        fis = None
        try:
            fis = open("a.txt")
        except OSError as e:
            print(e.strerror)
            return #方法返回前执行了finally块
            #os._exit(1) #退出解释器，不执行finally块
        #不管try块中是否出现异常，也不管哪个except块被执行，甚至执行了return语句，finally块总会被执行
        finally:
            if fis is not None:
                try:
                    fis.close()
                except OSError as e:
                    print(e.strerror)
            print("执行finally块中的资源回收")
            #return #在finally块中执行return或raise方法会导致方法终止(不执行try块和except剩余语句)
    test()
    #异常处理嵌套
    try:
        s, b = input("输入两个数字：").split()
        try:
            result = int(b)/int(s)
        except ValueError:
            print("需要输入两个数字")
    except ZeroDivisionError:
        print("零不能作为除数")
    else:
        print("%.2f"%result)
    
    """   
    python允许程序自行引发异常，自行印发异常食用raise语句来完成
    1）单独一个raise。该语句引发当前上下文中捕获的异常，或默认引发RuntimeError异常
    2）raise后带一个异常类。该语句引发指定异常类的默认实例
    3）raise后带一个异常对象。该语句引发指定的异常对象
    """
    def main():
        try:
            mtd(3)
        except Exception as e:
            print("出现异常",e)
        mtd(3)
    
    def mtd(n):
        if n >0:
            raise ValueError("n的值大于零，不符合要求")
    main() #最后会显示异常的传播轨迹
# =============================================================================
# 
# =============================================================================
#自定义异常类
class AuctionException(Exception):pass
class AuctionTest:
    def __init__(self, init_price):
        self.init_price = init_price
    def bid(self, bid_price):
        d = 0.0
        try:
            d = float(bid_price)
        except Exception as e:
            print("转换出异常",e)
            raise AuctionException("价格只能是数字")
            #raise AuctionException(e) #输出原始错误信息
            #raise #单独使用raise语句可以自动引发当前块中捕获到的异常
        if self.init_price > d:
            raise AuctionException("价格太低，竞拍失败")
        initPrice = d
 
class SelfException(Exception):pass
       
def Chapter7_3():
    def foo(n):
        if n >0:
            raise AuctionException
    try:
        foo(2)
        print("good")
    except AuctionException:
        print("值大于零，不符合要求")
    
    #except和raise同时使用
    at = AuctionTest(20.4)
    try:
        at.bid("df")
        print(at.initPrice)
    except AuctionException as ae:
        print("main中捕获的异常",ae)
    except Exception as e: #再次捕获异常
        print("main中捕获到的异常",e)
    
    #异常传播轨迹
    import traceback
    def main():
        firstMethod()
    def firstMethod():
        secondMethod()
    def secondMethod():
        thirdMethod()
    def thirdMethod():
        raise SelfException("自定义异常信息")
    
    try:
        main()
    except:
        """
        print_exc([limit[, file]])
        print_exception(etype, value, tb[, limit[, file]])
        1）etype：指定异常类型
        2）value：指定异常值
        3）tb：指定异常的traceback信息
        4）limit：用于限制显示异常传播的层数
        5）file：指定将异常传播轨迹信息输出到指定文件中
        当程序处于except块中时，该except块所捕获的异常信息可通过sys对象来获取(自动获取)
        """
        traceback.print_exc() #将异常传播轨迹信息输出到控制台或指定文件中
        traceback.print_exc(file=open("log.txt",'a'))
  
if __name__ == '__main__':
    Chapter7_3()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    