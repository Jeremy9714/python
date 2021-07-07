# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 08:32:36 2020

@author: Chenyang
"""
from functools import *
class Apple:
    def __init__(self, color, weight):
        self.color = color
        self.weight = weight
    def info(self):
        pass
    #重写__repr__()方法
    def __repr__(self):
        return "Apple[color=" + self.color +\
        ", weight=" + str(self.weight) + "]"
    def __del__(self):
        print("Apple内存已回收")

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def __setattr__(self,name,value):
        print("设置%s属性"%name)
        if name == "size":
            self.width, self.height = value
        elif 0<value:
            self.__dict__[name] = value
        else:
            raise ValueError("数值不存在")
    def __getattr__(self,name):
        print("读取%s属性"%name)
        if name == "size":
            return self.width, self.height
        else:
            raise AttributeError("没有该属性")
    def __delattr__(self,name):
        print("删除%s属性"%name)
        if name == "size":
            self.__dict__["width"] = 0
            self.__dict__["height"] = 0
        
class Comment:
    def __init__(self, detail, view_times):
        self.detail = detail
        self.view_times = view_times
    def info(self):
        print("一条简单的评论，内容是%s"%self.detail)
    def __call__(self):
        print("执行Comment对象")
        
def Chapter8_1(): #python类的特殊方法
    #__repr__()是一个自我描述的方法，该方法总是返回该对象实现类的"类名+object at+内存地址"值
    a = Apple("red", 10)
    print(a)
    #析构方法__del__()采用自动引用计数方式来回收对象占用的空间，当引用计数变成0，python就会回收该对象
    #b = a
    del a
    print("-----------")
    #__dir__()方法返回包含对象内部所有属性(包括方法)名的序列
    c = Apple("green",5)
    print(c.__dir__())
    #当程序对某个对象执行dir(object)函数时，会将该对象的所有属性进行排序，然后包装成列表
    print(dir(c))
    
    #__dict__属性用于查看对象内部存储的所有属性名和属性值组成的字典；也可以通过字典语法来访问或修改属性的值
    print(c.__dict__)
    print(c.__dict__["color"])
    c.__dict__["weight"] = 23
    print(c.weight)
    
    """
    当程序操作(访问、设置、删除)对象的属性时，python系统同样会执行该对象特定的方法
    1) __getattribute__(self,name): 当程序访问对象的name属性时被自动调用
    2) __getattr__(self,name): 当程序访问对象的name属性且该属性不存在时被自动调用
    3) __setattr__(self,name,value): 当程序对对象的name属性赋值时被自动调用
    4) __delattr__(self,name): 当程序删除对象的name属性时被自动调用
    """
    r = Rectangle(3,4)
    print(r.size) #size不存在，触发__getattr__()方法
    r.size = 6, 8
    print(r.size)
    print(r.width) #不触发__getattr__()方法
    del r.size
    print(r.size)
    #r.weight = 0
    
    #动态操作属性
    """
    动态检查对象是否包含某些属性相关的方法
    1) hasattr(obj, name): 检查obj对象是否包含名为name的属性或方法
    2) getattr(object, name[, default]): 获取object对象中名为name的属性或方法
    3) setattr(object, name, value,/): 将object对象的name属性设为value 
    """
    print("-------------------------------")
    c = Comment("hello",1)
    print(hasattr(c,"detail"))
    print(getattr(c,"detail"))
    print(hasattr(c,"info"))
    print(getattr(c,"info")) #getattr()方法只能获取属性的属性值
    setattr(c,"detail","world") #name作为字符串输入
    print(c.detail, c.view_times)
    setattr(c,"test",100)
    print(c.test)
    def bar():
        print("this is bar")
    setattr(c,"info",bar) #setattr()函数可以对方法进行设置，也可以讲方法改为属性
    c.info()
    
    #通过判断属性(或方法)是否包含__call__属性来确定它是否可以调用
    print(hasattr(c.detail,"__call__"))
    print(hasattr(c.info,"__call__"))
    
    #obj(arg1, arg2, ...)是obj.__call__(arg1, arg2, ...)的快捷写法
    c.__call__() #添加一个__call__方法
    c()
# =============================================================================
# 
# =============================================================================
def check_key(key): #该函数用于检查序列的索引
        if not isinstance(key, int): raise TypeError("索引必须是整数")
        if key<0: raise IndexError("索引不能为负数")
        if key>=26**3: raise IndexError("索引最大值不能超过%d"%26**3)
        
class StringSeq:
    def __init__(self):
        self.__changed = {} #用于存储被修改的数据
        self.__deleted = [] #用于存储北删除的数据的索引
    def __len__(self):
        return 26**3
    def __getitem__(self,key):
        check_key(key)
        if key in self.__changed:
            return self.__changed[key]
        if key in self.__deleted:
            return None
        three = key//(26*26)
        two = (key-three*26*26)//26
        one = key%26
        return chr(65 + three) + chr(65 + two) + chr(65 + one)
    def __setitem__(self,key,value):
        check_key(key)
        self.__changed[key] = value
    def __delitem__(self, key):
        check_key(key)
        if key not in self.__deleted:
            self.__deleted.append(key)
        if key in self.__changed:
            del self.__changed[key]
    
class Fibs: #敌营一个斐波那契数列的迭代器
    def __init__(self,len):
         self.first = 0
         self.second = 1
         self.__len = len
    def __next__(self):
        if self.__len == 0: raise StopIteration
        self.first, self.second = self.second, self.first + self.second #完成数列计算
        self.__len -= 1
        return self.first
    def __iter__(self):
        return self

class ValueDict(dict): #定义一个新的字典类
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
    def getkeys(self, val):
        result = []
        for key, value in self.items():
            if value == val: result.append(key)
        return result
     
def Chapter8_2():
    #序列相关方法
    """
    1) __len__(self): 该方法的返回值决定序列中元素的个数
    2) __getitem__(self,key): 该方法获取指定索引对应的元素。该方法的key应该是整数值或slice对象
    3) __contains__(self,item): 该方法判断序列是否包含指定元素
    4) __setitem__(self,key,value): 该方法设置指定索引对应的元素。该方法的key应该是整数值或slice对象
    5) __delitem__(self,key): 该方法删除指定索引对应的元素
    """
    sq = StringSeq()
    print(len(sq))
    print(sq[26*26])
    print(sq[0])
    sq[0] = "ZZZ"
    print(sq[0])
    del sq[0]
    print(sq[0])
    
    #实现迭代器
    """
    迭代器需要两个方法
    1) __iter__(self): 该方法返回一个迭代器，迭代器必须包含一个__next__()方法，该方法返回迭代器的下一个元素
    2) __reversed__(self): 该方法主要为内建的reversed()反转函数提供支持
    """
    fibs = Fibs(10)
    print(next(fibs),end=',') #获取迭代器的下一个元素
    for i in fibs:
        print(i,end = ',')
    print()
    #可使用内置的iter()函数将列表、元组等转换为迭代器
    my_iter = iter([1,2,3])
    print(my_iter.__next__())
    print(next(my_iter))

    #扩展列表、元组和字典
    my_dict = ValueDict(语文=85,数学=100,英语=100)
    print(my_dict.getkeys(100)) #获取对应value的所有key
    my_dict["编程"] = 100
    print(my_dict.getkeys(100))
    
    #生成器
    """
    生成器和迭代器的功能非常相似，它也会提供__next__()方法；
    生成器和迭代器的区别在于: 迭代器通常是先定义一个迭代器类，然后通过创建实例来创建迭代器；
    而生成器则是先定义一个包含yield语句的函数，然后通过调用该函数来创建生成器
    """
    def test(val,step):
        print("函数开始执行")
        cur = 0
        for i in range(val):
            cur+=i*step
            """
            yield语句的作用有两点:
            1) 每次返回一个值(类似return)
            2) 冻结执行，程序每次执行到yield语句时就会被暂停
            """
            yield cur
        
    t = test(10,2) #执行函数，返回生成器
    print("-------------------")
    print(next(t)) #第一次调用next()方法时，生成器函数才开始执行
    print(next(t)) #程序被yield语句冻结之后，当程序再次调用next()函数时，程序才会继续向下执行
    for ele in t:
        print(ele, end = ',')
    #可以将生成器转换为列表或元组
    t = test(10,3)
    print(list(t))
    t = test(10,4)
    print(tuple(t))
    print()
    
    #生成器的方法
    def square_gen(val):
        i=0
        out_val=None
        while True:
            #使用yield语句生成值，out_val用于接收send()方法发送的参数值
            out_val = (yield out_val**2) if out_val is not None else (yield i**2)
            if out_val is not None: print("======%d"%out_val)
            i+=1
    sg = square_gen(5)
    print(sg.send(None)) #生成器不能获取第一次调用send()方法发送的参数值
    print(next(sg))
    print("-------------------------")
    print(sg.send(9))
    print(sg.__next__())
    """
    1) close(): 该方法用于停止生成器
    2) throw(): 该方法用于在生成器内部(yield语句内)引发一个异常
    """
    #sg.throw(ValueError)
    sg.close() 
    #print(next(sg)) #生成器关闭后，程序不能再去获取生成器的下一个值
# =============================================================================
#     
# =============================================================================
class Square:
    def __init__(self,width, height):
        self.width = width
        self.height = height
    def setSize(self,size):
        self.width, self.height = size
    def getSize(self):
        return self.width, self.height
    Size = property(getSize, setSize)
    #重载加法
    def __add__(self,other):
        if not isinstance(other, Square):
            raise TypeError("不是一个类型")
        return Square(self.width+other.width,self.height+other.height)
    def __radd__(self,other):
        if not isinstance(other, int) or isinstance(other, float):
            raise TypeError("必须是数字")
        return Square(self.width+other, self.height+other)
    def __iadd__(self, other):
        if not isinstance(other, int) or isinstance(other, float):
            raise TypeError("必须是数字")
        return Square(self.width+other, self.height+other)
    def __gt__(self,other):
        if not isinstance(other, Square):
            raise TypeError("不是一个类型")
        return self.width*self.height>other.width*other.height
    def __ge__(self,other):
        if not isinstance(other, Square):
            raise TypeError("不是一个类型")
        return self.width*self.height>=other.width*other.height
    def __eq__(self,other):
        if not isinstance(other, Square):
            raise TypeError("不是一个类型")
        return self.width*self.height==other.width*other.height
    def __neg__(self):
        self.width, self.height = self.height, self.width
    def __float__(self):
        return float(self.width*self.height)
    def __repr__(self):
        return "square(width=%d, height=%d)"%(self.width,self.height)
    
def Chapter8_3():
    #运算符重载
    """
    __add__(self,other)：为"+"运算符提供支持
    __sub__(self,other)：为"-"运算符提供支持
    __mul__(self,other)：为"*"运算符提供支持
    __truediv__(self,other)：为"/"运算符提供支持
    __floordiv__(self,other)：为"//"运算符提供支持
    '''
    """
    s1 = Square(3,4)
    s2 = Square(5,6)
    print(s1+s2)
    """
    当程序执行x+y时，python会首先尝试使用x的__add__方法进行计算；如果x没有提供__add__方法，
    python还会尝试调用y的__add__方法进行计算;如果自定义类提供了__rxxx__方法，name该自定义
    类的对象就可以出现在对应运算符的右边
    __radd__(self,other)：为"+"运算符提供支持(y提供该方法)
    __rsub__(self,other)：为"-"运算符提供支持(y提供该方法)
    __rmul__(self,other)：为"*"运算符提供支持(y提供该方法)
    __rtruediv__(self,other)：为"/"运算符提供支持(y提供该方法)
    __rfloordiv__(self,other)：为"//"运算符提供支持(y提供该方法)
    ...
    """
    s = Square(10,10)
    print(2+s)
    print(s.Size)
    """
    __iadd__(self,other)：为"+="运算符提供支持
    __isub__(self,other)：为"-="运算符提供支持
    __imul__(self,other)：为"*="运算符提供支持
    __itruediv__(self,other)：为"/="运算符提供支持
    __ifloordiv__(self,other)：为"//="运算符提供支持
    '''
    """
    s+=2 #重载"+="运算符
    print(s)
    """
    __lt__(self,other)：为"<"运算符提供支持
    __le__(self,other)：为"<="运算符提供支持
    __gt__(self,other)：为">"运算符提供支持
    __ge__(self,other)：为">="运算符提供支持
    __eq__(self,other)：为"=="运算符提供支持
    __ne__(self,other)：为"!="运算符提供支持
    """
    s1 = Square(3,4)
    s2 = Square(2,7)
    print(s1==s2) #重载比较运算符
    print(s1<=s2)
    print(s1<s2)
    """
    __neg__(self)：为单目求负"-"运算符提供支持
    __pos__(self)：为单目求正"+"运算符提供支持
    __invert__(self)：为单目求反"~"运算符提供支持
    """
    -s1 #重载单目运算符
    print(s1)
    """
    __str__(self)：将对象转换成str对象
    __int__(self)：将对象转换成int对象
    __bytes__(self)：将对象转换成bytes对象
    __float__(self)：将对象转换成float对象
    __complex__(self)：将对象转换成complex对象
    """
    print(float(s2)) #重载类型转换符
# =============================================================================
# 
# =============================================================================
#from all_module import * #该语法只能在最模块外层执行，不能再函数内执行
def Chapter9_1(): #模块和包
    """
    使用import导入模块的语法主要有两种用法
    1) import 模块名1[as 别名1], 模块名2[as 别名2]...
    2) from 模块名 import 成员名1[as 别名1], 成员名2[as 别名2]
    * 第一种import语句导入模块内的所有成员；第二种import语句只导入模块内的指定成员
    * 当使用第一种import语句导入模块中的成员时，必须添加模块名或模块别名前缀
    """
    import sys as s, os as o
    print(s.argv[0]) #sys模块下的argv变量用于获取运行python程序的命令行参数
    print(o.sep) #os模块的sep变量代表平台上的路径分隔符
    from sys import argv as v
    print(v[0])
    from sys import argv, winver
    print(winver) #winver成员记录的python的版本号
    print(argv[0])
    
    #定义模块
    #模块就是python程序，任何python程序都可以作为模块导入。对于任何程序，只要导入了模块，即可使用该模块内的所有成员
    import module1 as m1
    #import module1 as m1 #当程序重复导入同一个模块时，python只会导入一次
    print(m1.my_book)
    m1.say_hi("charlie")
    user = m1.User("test")
    user.walk()
    print(user)
    
    #加载模块
    import sys, pprint
    #如果要打印的内容很多，使用pprint模块下的pprint()函数可以显示更友好的打印结果
    pprint.pprint(sys.path) #sys模块下的path变量代表python默认的模块加载路径
    #sys.path.remove('D:\\Desktop\\Scripts\\Python')
    import fk_module as fk#导入模块的本质就是: 将模块中的全部代码加载到内存并执行，然后将整个模块内容赋值给与模块同名的变量
    print("==============")
    print(type(fk))
    print(fk)
    #使用from...import...导入模块中成员的本质就是:将模块中的全部代码加载到内存并执行，然后只导入指定变量、函数等成员单元
    from fk_module import name, hello
    print("==============")
    print(name, hello,sep="\n")
    """
    在导入模块后，可以在模块文件所在目录下看到一个名为"__pycache__"的文件夹，
    里面是python为模块编译生成的字节码，用于提升该模块的运行效率
    """
    #模块的__all__变量
    #Ahello()
    #Aworld()
    #test() #由于该模块包含了__all__变量，因此只能导入__all__变量所列出的程序单元
    #可以通过import package_name和from package_name import...方法来导入__all__列表外的程序单元
    from all_module import Atest
    Atest() #不受__all__变量影响
# =============================================================================
# 
# =============================================================================
def Chapter9_2():
    #使用包
    """
    从物理上看，包就是一个文件夹，在该文件夹下包含了一个__init__.py文件，该
    文件夹可用于包含多个模块源文件；从逻辑上看，包的本质依然是模块(包也可以
    用于包含包)；定义包主要有两步
    1) 创建一个文件夹，该文件夹的名字就是该包的包名
    2) 在该文件夹内添加一个__init__.py文件
    """
    import first_package #将整个包的文件内容赋值给与包同名的变量(对象)
    print("=============")
    #导入包后，程序执行了该包所对应的文件夹下__init__.py
    print(first_package.__doc__) 
    print(type(first_package))
    print(first_package)
    #导入包内成员
    import fk_package #实际上就是导入fk_package包下的__init__.py
    import fk_package.print_shape #实际上就是导入fk_package包下的print_shape模块
    from fk_package import billing #实际上就是导入fk_package包下的billing模块
    import fk_package.arithmetic_chart #实际上就是导入fk_package包下的arithmetic_chart模块
    fk_package.print_shape.print_blank_triangle(6)
    print(billing.Item(4.5))
    fk_package.arithmetic_chart.print_arithmetic_chart(5)
    
    import fk_package as fk
    #__init__.py文件执行了导入后，它们会把所有模块中的程序单元导入包中
    fk.print_blank_triangle(6)
    im = fk.Item(4.5)
    print(im)
    fk.print_arithmetic_chart(5)
    
    #查看模块内容
    import string
    print(dir(string))
    print([e for e in dir(string) if not e.startswith('__')]) #输出所有非隐藏内容
    print(string.__all__) #__all__变量相当于模块开放的接口
    print()
    #使用__doc__属性查看文档
    #capwords(string [, sep=None]) 此方法将字符串中的每个单词的首字母大写。sep参数用来指定分隔符
    print(help(string.capwords)) #相当于访问程序单元的__doc__属性
    """
    使用help()函数之所以能查到程序单元的帮助信息，其实完全是因为该
    程序单元本身有文档信息，也就是有__doc__属性
    """
    print(string.capwords.__doc__)
    print(string.capwords("ab;cd",sep=";"))
    
    #使用__file__属性查看模块的源文件路径
    print(fk.__file__) #有些底层交互的模块可能不适用python编写的，因此这种模块不具有__file__属性
# =============================================================================
# 
# =============================================================================
def Chapter10_1(): #常见模块
    """
    sys模块代表了python解释器，主要用于获取和python解释器相关的信息   
    """
    import sys
    print([e for e in dir(sys) if not e.startswith("_")])
    print(sys.byteorder) #显示本地字节序的指示符
    print(sys.copyright) #显示与python解释器有关的版权信息
    print(sys.executable) #显示python解释器在磁盘上的存储路径
    print(sys.getfilesystemencoding) #显示在当前系统中保存文件所用的字符集
    print(sys.maxsize) #显示python整数支持的最大值
    print(sys.platform) #显示python解释器所在平台的指示符
    print(sys.version) #显示python解释器的版本信息
    print(sys.winver) #显示当前python解释器的主版本号
    #获取命令行参数
    print(len(sys.argv))
    for arg in sys.argv:
        print(arg)
    #sys.path.append("D:\\Desktop\\Scripts\\Python") #用于在程序运行时为python动态修改模块加载路径
    
    """
    os模块代表了程序所在的操作系统，主要用于获取程序运行所在操作系统的相关信息
    此外，在os模块下还包含大量进程管理函数，它们可用于启动新进程、中止已有进程等
    """
    import os
    print(os.__all__)
    print(os.name) #显示导入依赖模块的操作系统名称
    #print(os.environ) #显示当前系统上所有环境变量组成的字典
    print(os.getenv('CLASSPATH')) #获取指定环境变量的值
    print(os.getlogin()) #返回当前系统的登录用户名
    print(os.getpid()) #返回当前进程id
    print(os.getppid()) #返回当前进程的父进程id
    print(os.cpu_count()) #返回当前系统的cpu数量
    print(os.sep) #返回路径分隔符
    print(os.pathsep) #返回当前系统的路径分隔符
    print(os.linesep) #返回当前系统的换行符("\r\n")
    print(os.urandom(3)) #返回适合作为加密使用的、最多由N个字节组成的bytes对象
    #os.system("cmd") #运行操作系统上的指定命令；新程序所在的进程会替代原有的进程
    #os.startfile(path[, operation]): 对指定文件使用该文件关联的工具执行operation对应的操作(操作必须是有效的命令行操作项目)
    #os.spawnl(mode, path,...): 该函数用于在新进程中执行新程序
    #os.excel(path, arg0, arg1,...): 使用参数列表arg0,arg1,...来执行path所代表的执行文件；该函数运行新进程之后，也会取代原有进程
    
    """
    random模块主要包含生成伪随机数的各种功能变量和函数
    """
    import random
    print(random.__all__)
    print(random.random()) #生成一个在[0.0,1.0)之间的伪随机浮点数
    print(random.uniform(2.5, 6.0)) #生成一个范围在[a,b]之间的伪随机浮点数
    print(random.expovariate(1/-5)) #生成呈指数分布的伪随机浮点数；其中lambd参数为1除以期望平均值。如果lambd是正值，则返回的随机数是0到正无穷大；反之亦然
    print(random.randrange(2,10,3)) #生成一个在[start, end[, step])中的伪随机整数
    print(random.choice(["python", "c++", "java"])) #从seq中随机抽取一个元素
    a_list = [1,2,3,4,5]
    #random.choices(population, weights=None, cum_weights=None, k=1)
    #population: 集群； weights: 权重； cum_weights: 累加权重； k: 抽取次数
    print(random.choices(a_list, k=5))
    print(random.choices(a_list, weights=[0,0,1,0,1], k=5))
    print(random.choices(a_list, cum_weights=[0,1,1,1,1], k=5))
    random.shuffle(a_list) #对序列进行随机排列(无返回值)
    print(a_list)
    print(random.sample(a_list, k=3)) #从序列中随机抽取k个独立的元素(抽取到的元素不会放回)
    
    import collections
    print(random.choices(["python","c++","java"],[5,5,1],k=6))
    #模拟从牌堆抽取20张牌，牌面大于10的牌占多大比例
    deck = collections.Counter(tens=16,low_cards=36)
    seen = random.sample(list(deck.elements()),k=20)
    print(seen.count("tens"))
# =============================================================================
# 
# =============================================================================
import json
class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, complex):
            return {"complex":True,"real":obj.real,"imag":obj.imag}
        return json.JSONEncoder.default(self,obj)

def Chapter10_2():
    """
    time模块主要包含各种提供日期、时间功能的类和函数。该模块既提供了把日期、时间格式
    转化为字符串的功能，也提供了从字符串回复日期、时间的功能
    """
    import time
    print([e for e in dir(time) if not e.startswith("_")])
    """
    在time模块内提供了一个time.struct_time类，该类代表一个时间对象，它主要包含九个属性
    1) tm_year: 年 -> 20xx
    2) tm_mon: 月 -> [1,12]
    3) tm_mday: 日 -> [1,31]
    4) tm_hour: 时 -> [0,23]
    5) tm_min: 分 -> [0,59]
    6) tm_sec: 秒 -> [0,59]
    7) tm_wday: 一周内第几天 -> [0,6]
    8) tm_yday: 一年内第几天 -> [1,366]
    9) tm_isdst: 夏令时(daylight saving time) -> 0、1或-1 
    python可以使用time.struct_time(tm_year=2000,...)来代表时间，此外python还可以使用
    一个包含9个元素的元组来代表时间，该元组的九个元素和struct_time对象中九个属性的含义
    是一一对应的
    """
    #time.asctime([t]): 将时间元组或struct_time对象转换时间字符串.不指定参数t,则默认转换当前时间
    print(time.asctime((1997,7,14,6,0,0,0,200,0)))
    print(time.ctime()) #将以秒数代表的时间转换为时间字符串
    print(time.gmtime(30000)) #将以秒数代表的时间转换为struct_time对象。不传入参数则使用当前时间
    st = time.localtime(30000)
    print(time.localtime(30000)) #将以秒数代表的时间转换为代表当前时间的struct_time对象。不传入参数则使用当前时间
    print(time.mktime(st)) #localtime()的反转函数，用于将struct_time对象或元组代表的时间转换为从1970年一月一日0点整到当前时间经过的秒数
    print(time.perf_counter()) #返回性能计数器的值
    print(time.process_time()) #返回当前进程使用cpu的时间(以秒为单位)
    print(time.sleep(1)) #暂停sec秒
    print(time.time()) #返回从1970年一月一日零点整至今经过的秒数
    print(time.timezone) #返回本地时区的时间偏移，以秒为单位
    print(time.tzname) #返回本地时区的名字
    """
    python时间格式字符串
    %Y: 年份的完整形式
    %m: 代表月份的数值
    %d: 代表一个月中第几天的数值
    %H: 代表24小时制的小时
    %I: 代表12小时制的小时
    %M: 代表分钟的数值
    %S: 代表秒数的数值
    '''
    """
    #strftime()函数将时间元组或struct_time对象个是华为指定格式的时间字符串
    print(time.strftime("%Y-%m-%d: %H-%M-%S")) #不指定参数，默认转换当前时间
    #strptime()函数将字符串格式的时间解析成struct_time对象
    st = "2020年6月27日: 12点20分0秒"
    print(time.strptime(st,"%Y年%m月%d日: %H点%M分%S秒"))
    
    #JSON支持
    """
    JSON是一种轻量级、跨平台、跨语言的数据交换格式，JSON格式被广泛应用于各种语言的
    数据交换中。JSON主要有两种数据结构：由key-value对组成的数据结构；有序数列
    
    json模块提供了将符合格式的JSON字符串恢复成对象的函数，也提供了将python对象转换
    成JSON字符串的函数。JSON类型到python类型的转换关系如下
    1) 对象object -> 字典dict
    2) 数组array -> 列表list
    3) 字符串string -> 字符串str
    4) 整数number(int) -> 整数int
    5) 实数number(real) -> 浮点数float
    6) true、false、null -> True、False、None
    当程序把python对象转换成JSON格式字符串时，转换关系如下
    1) 字典dict -> 对象object
    2) 列表list和元组tuple -> 数组array
    3) 字符串str -> 字符串string
    4) 整型、浮点型、以及整型、浮点型派生的枚举 -> 数值型number
    5) True、False、None -> true、false、null
    """
    #import json
    print(json.__all__)
    #json.dumps(obj,...) 将obj对象转换为JSON字符串，并返回该字符串
    s = json.dumps(["yeeku",{"favorite":("coding",None,"game",25)}])
    print(s)
    s2 = json.dumps("\"foo\bar")
    print(s2)
    s3 = json.dumps({"c":0,"b":1,"a":2}, sort_keys = True) #将字典对象转换为JSON字符串，并对key排序
    print(s3)
    s4 = json.dumps([1,2,3,{'x':5,'y':7}],separators = (',',':')) #指定分隔符
    print(s4)
    s5 = json.dumps({"python":5,"kotlin":7},sort_keys=True, indent=4) #指定转换的JSON字符串的缩进
    print(s5)
    #JSONEncoder的encode()方法将python对象转换为JSON字符串
    s6 = json.JSONEncoder().encode({"name":("孙悟空","齐天大圣")})
    print(s6)
    f = open("a.json", 'w')
    #将转换得到的JSON字符串输出到文件中
    json.dump(["kotlin",{"python":"excellent"}],f)
    
    result1 = json.loads('["yeeku",{"favorite":["coding",null,"game",25]}]')
    print(result1)
    result2 = json.loads('"\\"foo\\"bar"')
    print(result2)
    def as_complex(dct):
        if "__complex__" in dct:
            return complex(dct["real"],dct["imag"])
        return dct
    
    #object_hook参数用于指定函数，该函数负责把反序列化后的基本类型对象转换成自定义类型的对象
    result3 = json.loads('{"__complex__":true,"real":1,"imag":2}',object_hook = as_complex)
    print(result3)
    def sorted_list(lst):
        return sorted(lst)
    result4 = json.loads('[2,12,44,100]',object_hook = sorted_list)
    print(result4)
    f = open("a.json")
    result5 = json.load(f) #从文件流恢复JSON列表
    print(result5)
    
    #扩展JSONEncoder类来完成从python特殊类型到JSON类型的转换
    f2 = open("b.json",'w')
    json.dump(2+1j,f2,cls=ComplexEncoder)
    f2.close()
    #扩展JSONEncoder类的子类，并重写了它的default()方法，方法判断如果要转换的目标类型为复数，程序就会对其进行自定义转换
    s1 = json.dumps(2+1j, cls=ComplexEncoder) #通过cls属性指定使用JSONEncoder的自定义子类
    print(s1)
    s2 = ComplexEncoder().encode(2+1j) #直接使用JSONEncoder的自定义子类的encode()方法来进行转换
    print(s2)
# =============================================================================
# 
# =============================================================================
def Chapter10_3():
    """
    正则表达式用于描述一种字符串匹配模式(pattern)，它可以用于检查一个字符串是否
    含有某个字串，也可以用于从字符串中提取匹配的字串，或者对字符串中匹配的字串进
    行替换操作
    """
    import re
    print(re.__all__)
    """
    1) re.compile(pattern, flags=0):该函数用于将正则表达式字符串
    编译成_sre.SRE_Pattern对象，该对象代表了正则表达式编译之后在内
    存中的对象
    2) re.match(pattern, string, flags=0):尝试从字符串的开始位置
    来匹配正则表达式，如果从开始位置匹配不成功，则返回None.该函数返
    回_sre.Sre_Match对象，该对象包含的span(n)方法用于获取第n+1个组
    的匹配位置(区间)，group(n)方法用于获取第n+1个组所匹配的子串
    3) re.search(pattern, string, flags=0):扫描整个字符串，并返回
    字符串中第一处匹配pattern的匹配对象
    """
    p = re.compile("abc")
    p.search("www.abc.com")  #_sre.Sre_Pattern对象的search()方法执行匹配(该方法可以缓存正则表达式字符串，具有更好的性能)
    re.search("abc","www.abc.com") #直接使用正则表达式匹配目标字符串
    m1 = re.match("www","www.fkit.com\id=www\s") #从开始位置匹配
    print(m1.span(0),m1.group(0))
    print(re.match("fkit","www.fkit.com")) #开始位置匹配不到，返回None
    m2 = re.search("fkit","www.fkit.com")
    print(m2.span(),m2.group())
    
    """
    re.findall(pattern, string, flags=0):扫描整个字符串，并返回
    字符串中所有匹配pattern的子串组成的列表
    re.finditer(pattern, string, flags=0):扫描整个字符串，并返回
    字符串中所有匹配pattern的子串组成的迭代器，迭代器的元素是_sre.Sre_Match
    对象
    """
    print(re.findall("fkit","Fkit is very good, Fkit.org is my favorite",re.I))
    it = re.finditer("fkit","Fkit is very good, Fkit.org is my favorite",re.I)
    for e in it:
        print(e.span(), e.group())
    """
    re.fullmatch(pattern, string, flags=0):该函数要求整个字符串
    能匹配pattern,如果匹配则返回包含匹配信息的_sre.Sre_Match对象；
    否则返回None
    re.sub(pattern, repl, string, count=0, flags=0):该函数用于将
    string字符串中所有匹配pattern的内容替换成repl；repl既可以是被替
    换的字符串，也可以是一个函数。count参数控制最多替换次数，如果为0，
    则表示全部替换
    """
    print(re.fullmatch("fkit","www.fkit.com"))
    print(re.fullmatch('a','a'))
    my_date = "2008-08-18"
    print(re.sub(r'-','/',my_date,1))
    def fun(matched):
        value = r"<疯狂" + (matched.group("lang")) +r"讲义>"
        return value
    s = "python很好，kotlin也很好"
    """
    该正则表达式用圆括号表达式创建了一个组，并用'?P'选项为该组起名为lang
    所起的组名要放在尖括号里。"\w"带包任意字符，'+'用于限定前面的"\w"可
    出现一到多次。由于sub()函数指定了re.A选项，这样"\w"就只能代表ASCII字
    符，不能代表汉字
    """
    print(re.sub(r"(?P<lang>\w+)",fun,s,flags=re.A))
    
    """
    re.split(pattern, string, maxsplit=0, flags=0):使用pattern对string
    进行分割，该函数返回分割得到的多个子串组成的列表。其中maxsplit参数控制
    最多分割几次
    """
    print(re.split(', ',"fkit, fkjava, crazyit", 1))
    print(re.split('x', "fkit")) #没有匹配内容则不会进行分割
    re.purge() #清除正则表达式缓存
    #re.escape(pattern): 对pattern中除ASCII字符、数值、下划线以外的其他字符进行转义
    print(re.escape(r'www.crazyit.org is good, i love it'))
    pa = re.compile('fkit')
    
    #正则表达式对象的方法可以指定pos和endpos参数
    print(pa.match("www.fkit.com",4,8)) #在索引区间执行匹配
    print(pa.fullmatch("www.fkit.com",4,8))
    print(pa.match("www.fkit.com",4,8).endpos)
    
    """
    re模块中的Match对象包含了详细的正则表达式匹配信息，包括正则表达式
    匹配的位置、正则表达式所匹配的子串
    1) match.group([group1]...):获取该匹配对象中指定组所匹配的字符串
    2) match.__getitem__(g):这是match.group(g)的简化写法，程序可使用match[g]
    3) match.groups(default=None):返回match对象中所有组所匹配的字符串组成的元组
    4) match.groupdict(default=None):返回match对象中所有组所匹配的字符串组成的字典
    5) match.start([group])、end([group])、span([group]):获取该匹配对象中指定组所匹配的字符串的开始、结束位置
    """
    #如果正则表达式中没有括号，那么整个表达式就属于一个默认组
    m = re.search(r'(fkit).(org)',r"www.fkit.org is a good domain")
    #该正则表达式含有两个组
    print(m[0],m.span(0)) #group(0)是整个正则表达式所匹配的字串
    print(m[1],m.span(1)) #第一个组所匹配的字串
    print(m[2],m.span(2)) #第二个组所匹配的字串
    print(m.groups())
    print(m.start(1))
    
    #'?P<group_name>'为正则表达式的组指定名字
    m2 = re.search(r'(?P<prefix>fkit).(?P<suffix>org)',\
                   r"www.fkit.org is a good domain")
    print(m2.groupdict())
    print(m2.re) #返回执行正则表达式匹配时所用的正则表达式
    print(m2.string) #返回执行正则表达式匹配时所用的字符串
    print(m2.lastgroup,m2.lastindex)
    
    #正则表达式旗标
    """
    python支持的正则表达式旗标都使用该模块中的属性来代表
    1) re.A或re.ASCII:该旗标控制\w,\W,\b,\B,\d,\D,\s,\S只匹配ASCII字符。可以在正则
    表达式中使用行内旗标(?a)来代表
    2) re.DEBUG:显示编译正则表达式的Debug信息
    3) re.I或re.IGNORECASE:使用正则表达式匹配时不区分大小写。行内旗标(?i)
    4) re.L或re.LOCALE:根据当前区域设置使用正则表达式匹配时不区分大小写。行内旗标(?L)
    5) re.M或re.MULTIPLE:多行模式的旗标。当指定该旗标后，'^'能匹配字符串的开头(换行符
    之后)和每行的开头，'$'能匹配字符串的末尾(换行符之前)和每行的末尾。行内旗标(?m)
    6) re.S或re.DOTALL:让点'.'能匹配包含换行符在内的所有字符。行内旗标(?s)
    7) re.X或re.VERBOSE:通过该旗标允许分行书写正则表达式，也允许为正则表达式添加注释。
    行内旗标(?x)
    """
    rl = re.findall(r'fkit',"www.Fkit.com is fkit",re.I) #无视大小写
    print(rl)
    a = re.compile(r"""020 #广州的区号
                  \-      #中间的短横线
                  \d{8}   #八个数值""",re.X)
    print(a.match("020-123456789").group())
# =============================================================================
#   
# =============================================================================
def Chapter10_4():
    #创建正则表达式
    """
    正则表达式中的合法字符:
    1) x -> 字符x
    2) \\uhhhh -> 十六进制值0xhhhh所表示的Unicode字符
    3) \f -> 换页符
    4) \t -> 制表符
    5) \n -> 换行符
    6) \r -> 回车符
    7) \a ->报警
    8) \e -> Escape符
    9) \cx -> x对应的控制符   
        
    正则表达式中的特殊字符:
    1) & -> 匹配一行的结尾
    2) ^ -> 匹配一行的开头
    3) () -> 匹配子表达式(组)的开始位置和结束位置
    4) [] -> 用于确定中括号表达式的开始位置和结束位置
    5) {} -> 用于标记前面子表达式的出现频度
    6) * -> 指定前面子表达式可以出现零次或多次
    7) + -> 指定前面子表达式可以出现一次或多次
    8) ? -> 指定前面子表达式可以出现零次或一次
    9) . -> 匹配出换行符外所有的字符
    10) \ -> 用于转义下一个字符，或指定八进制、十六进制字符
    11) | -> 指定在两项之间任选一项
    """
    import re
    print(re.fullmatch(r'.?\[',"?[").group())
    
    """
    正则表达式中的预定义字符:
    1) \d -> 匹配0~9所有数字
    2) \D -> 匹配非数字
    3) \s -> 匹配所有的空白字符，包括空格、制表符、回车符、换页符、换行符等
    4) \S -> 匹配所有非空白字符
    5) \w -> 匹配所有的单词字符，包括0~9数字、26个英文字母和下划线(_)
    6) \W -> 匹配所有的非单词字符
    """
    print(re.fullmatch(r'\d{3}-\d{4}-\d{4}', "078-3820-2351"))
    
    """
    方括号表达式:
    1) 表示枚举: [abc],表示a、b、c任意一个字符
    2) 表示范围: [a-z],表示a~z范围内的任意字符。范围可以和枚举结合使用，[a-cx-z]，表示a~c、x~z范围内的任意字符
    3) 表示求否^: [^abc],表示非a、b、c的任意字符
    
    边界匹配符:
    1) ^ -> 行的开头
    2) $ -> 行的结尾
    3) \b -> 单词的边界，即只能匹配单词前后的空白
    4) \B -> 非单词的边界，即只能匹配不在单词前后的空白
    5) \A -> 只匹配字符串的开头
    6) \Z -> 只匹配字符串的结尾，仅用于最后的结束符
    """
    
    #子表达式
    #[\w ]表示可以匹配任意单词字符和空格；'\1'引用第一个捕获组所匹配的字符串
    m = re.match(r'Windows (95|98|NT|2000)[\w ]+\1', "Windows 98 published in 98")
    print(m.group())
    """
    
    1) (?P<name>exp):匹配exp表达式并捕获成命名组，该组的名字为name。后面可以通过
    (?P=name)来引用前面捕获的组
    2) (?:exp):匹配exp表达式并且不捕获。不能通过\1、\2来引用
    3) (?<=exp):括号中的子模式必须出现在匹配内容的左侧，但exp不作为匹配的一部分
    4) (?=exp):括号中的子模式必须出现在匹配内容的右侧。但exp不作为匹配的一部分
    5) (?<!exp):括号中的子模式必须不出现在匹配内容的左侧
    6) (?=!exp):括号内的子模式必须不出现在匹配内容的右侧
    7) (?#comment):'?#'后面的内容是注释，不影响正则表达式本身
    8) (?aiLmsux):旗标组，用于为整个正则表达式添加行内旗标，可同时指定一个或多个
    9) (?imsx-imsx:exp):只对当前组起作用的旗标。如果在旗标前应用'-'，则表明去掉该旗标
    """
    print(re.search(r'<(?P<tag>\w+)>\w+</(?P=tag)>',"<h3>xxx</h3>"))
    print(re.search(r'Windows (?:95|98|NT|2000)[a-z ]+',"Windows 98 published in 98"))
    print(re.search(r'(?<=<h1>).+?(?=</h1>)',"<h1>fkit.org</h1> technology")) #.+?表示任意字符出现一到多次，但是要尽可能的少
    print(re.search(r'[a-zA-Z0-9_]{3,}(?#username)@fkit.org',"jeremy@fkit.org"))
    print(re.search(r"""(?ix)[a-z0-9_]+?(?#username)
                    @gmail.com     #八个数值""","Jeremy@gmail.com"))
    print(re.search(r'(?i:[a-z0-9]){3,}@fkit.org',"Sun@Fkit.org")) #只有组内表达式不区分大小写
    print(re.search(r'(?-i:[a-z0-9-]){3,}@gmail.com',"Sun@gmail.com",re.I))
    
    #贪婪模式和勉强模式
    """
    在默认情况下，正则表达式的频度限定式贪婪模式，就是指表达式中的模式会尽可能多的匹配字符；
    只要在频度限定之后添加一个英文符号，贪婪模式就变成了勉强模式，就是指表达式中的模式会尽
    可能少的匹配字符
    """
    print(re.search(r'@.+\.',"sun@fkit.com.cn")) #'.+'会尽可能多地匹配字符
    print(re.search(r'@.+?\.',"sun@fkit.com.cn"))
# =============================================================================
# 
# =============================================================================
def Chapter10_5():
    #容器相关类
    """
    set集合不记录元素的添加顺序，元素也不允许重复；set集合是可变容器，程序可以改变容器中的
    元素。与之对应的还有frozenset集合，frozenset集合是不可变容器，它的元素是不可变得
    """
    print([e for e in dir(set) if not e.startswith("_")])
    c = {"a","b","c"}
    c.discard("d") #如果集合中不包含被删除元素，该方法什么也不做
    #c.remove("d") #如果集合中不包含被删除元素，则会报出KeyError错误
    books = set()
    books.add("a")
    print(books)
    print(books<=c) #判断'<='前面的集合是否为后面集合的子集合
    print(books.issubset(c))
    print(c>=books) #判断'>='前面的集合是否为后面集合的父集合
    print(c.issuperset(books))
    result1 = c-books #相当于difference()
    print(result1)
    result2 = c.difference(books) #不改变集合本身
    print(result2)
    c.difference_update(books) #改变集合本身
    print(c)    
    c.clear()
    d = {"a","b","c"}
    inter1 = d & books
    print(inter1)
    inter2 = d.intersection(books) #交集
    print(inter2)
    d.intersection_update(books)
    print(inter2)
    e = set(range(5))
    f = set(range(3,7))
    print(e,f)
    xor = e^f #异或，属于a或属于b,但不同时属于a和b的元素
    print(xor)
    print(e.symmetric_difference(f)) #异或
    un = e.union(f) #并集，不改变集合本身
    print(un)
    e.update(f) #并集，改变集合本身
    print(e,'\n')
    
    #字典的key必须是不可变对象，因此只能用frozenset
    s = set()
    frozen_s = frozenset("kotlin")
    s.add(frozen_s) #可以向集合添加frozenset集合
    print(s)
    #s.add({"python"}) #不能向set集合添加普通set集合
    
    #双端队列deque
    from collections import deque
    print([e for e in dir(deque) if not e.startswith("_")])
    """
    将deque当成stack来使用
    """
    stack = deque(("a0","a1","a2")) #deque(iterable[, maxlen])
    print(stack)
    stack.append("a3")
    stack.extend(("a4","a5"))
    print(stack)
    stack.pop()
    stack.pop()
    #stack.appendleft("a")
    print(stack)
    """
    将deque当成list来使用
    """
    lst = deque(['a','b','c'])
    print(lst)
    lst.append('d')
    lst.extend(['e','f'])
    print(lst)
    lst.popleft()
    lst.popleft()
    print(lst)
    
    q = deque(range(5))
    print(q)
    q.rotate() #rotate()方法将队列的队尾元素移动到队头，使之首尾相连
    print(q)
    q.rotate()
    print(q)
# =============================================================================
# 
# =============================================================================
def Chapter10_6():
    """
    在一个含有n个元素的序列中，当且仅当满足如下关系时，可以将这组数据称为堆
    1) 小顶(根)堆: K(i)<=K(2i+1)且K(i)<=K(2i+2)
    2) 大顶(根)堆: K(i)>=K(2i+1)且K(i)>=K(2i+2)
    python提供的heapq包中有一些函数，当使用这些函数来操纵列表时，该列表就会表现出堆的行为
    """
    import heapq
    print(heapq.__all__)
    my_data = list(range(10))
    my_data.append(0.5)
    print(my_data)
    heapq.heapify(my_data) #heapify(heap)方法将堆属性应用到列表上
    print(my_data)
    heapq.heappush(my_data, 7.2) #heappush(heap,item)方法将item元素加入堆
    print(my_data)
    heapq.heappop(my_data) #将最小元素弹出
    heapq.heappop(my_data)
    print(my_data)
    
    #heapreplace(heap,item)方法先弹出堆中最小元素，并将元素item入堆;返回被弹出的元素
    print(heapq.heapreplace(my_data,8.1)) 
    print(my_data)
    #heappushpop(heap,item)方法先将item入堆,然后弹出并返回堆中最小的元素
    print(heapq.heappushpop(my_data,10))
    print(my_data)
    print(heapq.nlargest(3,my_data)) #返回堆中最大的n个元素
    print(heapq.nsmallest(4,my_data)) #返回堆中最小的n个元素
    
    my_data2 = list(range(4,12))
    heapq.heapify(my_data2)
    print(my_data2)
    for c in heapq.merge(my_data,my_data2): #将多个有序的堆合并成一个大的有序堆，然后再输出
        print(c,end=" ")
    print()
    #collections下的容器支持
    """
    ChainMap是一个方便的工具类，它使用链的方式经多个dict链在一起；由于多个dict并没有被真正
    的合并在一起，因此在多个dict中可以存在重复的key，在这种情况下，排在'链'前面的dict中的key
    具有更高的优先级
    """
    from collections import ChainMap
    #print(ChainMap.__doc__)
    a = {"kotlin":90,"python":86}
    b = {"go":93,"python":92}
    c = {"swift":89,"go":87}
    cm = ChainMap(a,b,c)
    print(cm)
    print(cm['python'])
    print(cm['go'])
    
    """
    collections包下的Counter类可以自动统计容器中各元素出现的次数
    Counter对象的本质就是一个特殊的dict，它的key都是其所包含的元素，而它的value则记录了该
    key出现的次数。如果通过Counter不存在的key访问value，则会输出0
    """
    from collections import Counter
    #print(Counter.__doc__)
    #c1 = Counter()
    #可以通过任何可迭代参数对象来构建Counter对象
    c = Counter("string")
    #c3 = Counter([1,2,3])
    #c4 = Counter({"a":2})
    c1 = Counter(a=1,b=2) #可以使用关键字语法来定义Counter对象
    print(c['s'])
    print(c1['b'])
    #Counter继承了dict类，它可以调用dict所支持的方法
    print(list(c.elements())) #该方法返回该Counter所包含全部元素的迭代器
    c = Counter("jeremy")
    print(c.most_common(1)) #返回Counter中出现最多的n个元素
    c = Counter(a=4,b=2,c=0,d=-2,e=5)
    d = Counter(a=1,b=2,c=3,d=4)
    c.subtract(d) #计算Counter的减法，计算减去之后各元素出现的次数
    print(dict(c))
    del c['e'] #删去key-value对
    print(c)
    
    c = Counter(python=4,swift=2,kotlin=3,go=-2)
    print(sum(c.values())) #dict.values()返回包含全部value列表的dict_values对象
    print(c)
    print(c.most_common()[:-4:-1])
    c.clear()
    
    #Counter对象运算
    c = Counter(a=3,b=1,c=-1)
    d = Counter(a=1,b=2,d=3)    
    print(c+d,c-d) #将两个Counter对象中各key出现的次数相运算，且只保留出现次数为正的元素
    print(c&d) #取两个Counter对象中都出现的key且各key对应的次数的最小数(正数)
    print(c|d) #取两个Counter对象中各key对应的出现次数的最大数(正数)
    print(+c) #只保留Counter对象中出现次数为0或正数的key-value对
    print(-c) #只保留Counter对象中出现次数负数的key-value对，并将出现次数改为正数
    
    #defaultdict对象
    """
    defaultdict是dict的子类。如果程序试图根据不存在的key来访问对应的value值，
    defaultdict可以提供一个default_factory属性，该属性所指定的函数负责为不存
    在的key来生成value
    """
    def foo():
        return 100
    from collections import defaultdict
    my_defaultdict = defaultdict(foo) #指定函数作为default_factory
    print(my_defaultdict['1'])
    
    s = [('a',2),('c',5),('a',6),('d',2)]
    d = {}
    #setdefault()函数用于获取指定key对应的value，如果key不存在，setdefault()方法就会先为该key设置一个默认的value
    for k,v in s:
        d.setdefault(k,[]).append(v)
    print(d)
    d=defaultdict(list)
    for k,v in s:
        d[k].append(v)
    print(list(d.items()))
    
    #nametuple工厂函数
    """
    nametuple()是一个工厂函数，使用该函数可以创建一个tuple类的子类，该子类可以
    为tuple的每一个元素指定字段名，程序可以通过字段名来访问namedtuple的各元素了。
    namedtuple(typename,field_names,*,verbose=False,renanme=False,module=None)
    1) typename:该参数指定所创建的tuple子类的类名
    2) field_names:该参数是一个字符串序列.多个字段名用空格、逗号隔开
    3) rename:如果该参数设为True,那么无效的字段名将会被自动替换为位置名('__0','__1')
    4) verbose:如果该参数被为True,那么当该子类被创建之后，该类定义就会被立即打印出来
    5) module:如果设置了该参数，那么该类将位于该模块下
    """
    from collections import namedtuple
    Point = namedtuple('Point','x y') #定义元组类
    p = Point(12,y=20)
    print(p[0]+p[1])
    print(p.x+p.y) #根据字段名访问各元素
    my_data=['East','North']
    p2 = Point._make(my_data) #_make(iterable)方法用于根据可迭代对象或序列创建命名元组对象
    print(p2)
    print(p2._asdict()) #将当前命名元组对象转换为OrderedDict字典
    p2._replace(x='South',y='West')#替换命名元组中一个或多个字段的值
    print(p2)
    print(p2._fields) #返回该命名元组中所有字段名组成的元组
    Color = namedtuple('Color','red green blue')
    Pixel = namedtuple('Pixel',Point._fields+Color._fields) #字段由别的类的字段组成
    p3 = Pixel(11,12,13,14,15)
    print(p3)
    
    #OrderedDict对象
    """
    OrderedDict是dict的子类，它可以维护添加key-value对的顺序。即使两个OrderedDict中
    的key-value对相同，但只要他们的顺序不同，程序在判断它们是否相等时会返回false
    """
    from collections import OrderedDict
    my_data={"python":20,"swift":32,"kotlin":43,"go":25}
    d1 = OrderedDict(sorted(my_data.items(),key=lambda f:f[0])) #按照key排序的字典
    d2 = OrderedDict(sorted(my_data.items(),key=lambda f:f[1])) #按照value排序的字典
    print(d1)
    print(d2)
    print(d1==d2)
    
    d = OrderedDict.fromkeys('abcde')
    print(d)
    #move_to_end(key,last=True)方法将指定的key-value对移动到最右边(最后加入);last=False时，将指定的key-value对移动到最左边(最先加入)
    d.move_to_end('c') 
    print(d)
    d.move_to_end('b',last=False)
    print(d.keys())
    print(d.popitem(last=False)) #默认弹出并返回最右边(最后加入)的key-value对;last=False反之亦然
# =============================================================================
#     
# =============================================================================
def Chapter10_7():
    #itertools模块
    import itertools as it
    print([e for e in dir(it) if not e.startswith("_")])
    for e in it.count(10,3): #count(start[,step])生成从start开始步长为step的迭代器
        print(e)
        if e>20:
            break
    my_count = 0
    for e in it.cycle("abcd"): #cycle(seq)生成对序列seq无限循环的迭代器
        print(e)
        my_count+=1
        if my_count>7:
            break
    for e in it.repeat("Python",3): #repeat(ele[,n])生成n个ele元素重复的迭代器
        print(e)
    #accumulate(seq[,func])生成根据序列元素累加的迭代器  
    for e in it.accumulate(range(1,10),lambda x,y:x*y):
        print(e)
    #chain()将多个元素里的序列链在一起生成新的序列
    for e in it.chain(('a','b'),[12,13]):
        print(e)
    #compress(data,selectors)根据selectors序列的值对data序列的元素进行过滤，对应的selectors的值为真则保留
    for e in it.compress(['a','b','c','d'],[1,1,0,0]):
        print(e)
    #dropwhile(func,seq)使用func函数对序列seq进行过滤，从第一个使func函数为false的元素开始，保留到从该元素到序列结束的全部元素
    for e in it.dropwhile(lambda x:len(x)<4,['a','b','abcde','aa','bb']):
        print(e)
    #takewhile(func,seq)与dropwhile()函数相反，去掉使func值为false的元素到序列末尾之间的全部元素
    for e in it.takewhile(lambda x:len(x)<4,['a','b','abcde','aa','bb']):
        print(e)
    #filterfalse(func, seq)保留所有使func为true的元素
    for e in it.filterfalse(lambda x:len(x)<4,['a','b','abcde','aa','bb']):
        print(e)
    #starmap(func,seq)使用func对序列seq进行计算，将计算结果作为新的序列元素；支持序列解包
    for e in it.starmap(pow,[(2,3),(3,4),(4,5)]):
        print(e)
    #zip(*p,fillvalue=None)将多个序列中的元素按照索引合并成元组,两个序列长度不等时可以设置默认值
    for e in it.zip_longest('ABCD','12',fillvalue='*'):
        print(e)
    #product(seq[,repeat=1])将序列中的元素进行嵌套循环排列组合
    for e in it.product('AB',repeat=2):
        print(e)
    print()
    #permutations(seq[,num])从序列中取出num个元素组成全排列
    for e in it.permutations('ABCD',2):
        print(''.join(e))
    print()
    #combinations(seq,num)从序列中取出num个元素组成全组合，元素不允许重复
    for e in it.combinations('ABCD',2):
        print(''.join(e))
    print()
    #combinations_with_replacement(seq,num)从序列中取出num个元素组成全组合，元素允许重复
    for e in it.combinations_with_replacement('ABCD',2):
        print(''.join(e))
# =============================================================================
# 
# =============================================================================

def Chapter10_8():
    #functools模块的功能函数
    print([e for e in dir(functools) if not e.startswith("_")])
    
    

if __name__ == '__main__':
    Chapter10_8()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    