# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 18:12:42 2020

@author: Chenyang
"""
import random
from tkinter import *

class Application(Frame):
    def __init__(self,master=None): 
        Frame.__init__(self,master)
        self.pack()
        self.initWidgets()
    def initWidgets(self):
        w = Label(self)
        bm = PhotoImage(file='images\\timg.png')
        w.x = bm
        w['image'] = bm
        w.pack()
        okButton = Button(self,text='确定')
        okButton.configure(background = 'yellow')
        #okButton = Button(self,text='确定',background='yellow')
        okButton.pack()

class App:
    def __init__(self,master):
        self.master = master
        self.initWidgets()
    def initWidgets(self):
        fm1=Frame(self.master)
        fm1.pack(side=LEFT,fill=BOTH,expand=YES)
        Button(fm1,text='第一个',bg='red').pack(side=TOP,fill=X,expand=YES)
        Button(fm1,text='第二个').pack(side=TOP,fill=X,expand=YES)
        Button(fm1,text='第三个').pack(side=TOP,fill=X,expand=YES)
        fm2=Frame(self.master)
        fm2.pack(side=LEFT,padx=10,expand=10)
        Button(fm2,text='第一个',fg='yellow').pack(side=RIGHT,fill=Y,expand=YES)
        Button(fm2,text='第二个').pack(side=RIGHT,fill=Y,expand=YES)
        Button(fm2,text='第三个').pack(side=RIGHT,fill=Y,expand=YES)
        fm3=Frame(self.master)
        fm3.pack(side=RIGHT,padx=10,fill=BOTH,expand=YES)
        Button(fm3,text='第一个').pack(side=BOTTOM,fill=Y,expand=YES)
        Button(fm3,text='第二个').pack(side=BOTTOM,fill=Y,expand=YES)
        Button(fm3,text='第三个').pack(side=BOTTOM,fill=Y,expand=YES)

class Apps:#grid布局管理器
    def __init__(self,master):
        self.master = master
        self.initWidgets()
    def initWidgets(self):
        #创建一个输入组件
        e = Entry(relief = SUNKEN,font=('Courier New',24),width=25)
        #对该输入组件进行布局
        e.pack(side=TOP,pady=10)
        p=Frame(self.master)
        p.pack(side=TOP)
        names=('0','1','2','3','4','5','6','7','8','9','+','-','*','/','.','=')
        for i in range(len(names)):
            b=Button(p,text=names[i],font=('Verdana',20),width=6)
            b.grid(row=i//4,column=i%4)   
            
class App2:
    def __init__(self,master):
        self.master=master
        self.initWidgets()
    def initWidgets(self):
        books = ('疯狂python讲义','疯狂swift讲义','疯狂kotlin讲义',\
                 '疯狂java讲义','疯狂ruby讲义')
        for i in range(len(books)):
            ct=[random.randrange(256) for x in range(3)]
            grayness = int(round(0.299*ct[0]+0.587*ct[1]+0.114*ct[2]))
            bg_color = '#%02x%02x%02x'%tuple(ct)
            lb = Label(self.master,
                       text=books[i],
                       fg = 'White' if grayness < 125 else 'Black',
                       bg = bg_color)
            lb.place(x=20,y=36+i*36,width=180,height=30)
            
    
def Chapter11_1():
    def Task1():
        root =  Tk() #Tk代表程序的主窗口
        root.title('窗口标题')
        w = Label(root,text='Hello Tkinter')
        w.pack() #布局
        root.mainloop()
        
    def Task2():
        app=Application()
        #当程序在创建任意Widget组件时没有指定master属性，那么程序会自动为该组件创建一个Tk窗口
        print(type(app.master))  
        app.master.title('窗口标题')
        app.mainloop()

    def Task3():
        root = Tk()
        root.title('Pack布局')
        for i in range(3):
            lab = Label(root, text="第%d个label"%(i+1),bg='white')
            lab.pack() #pack布局默认为垂直方向
        root.mainloop()
    #print(help(Label.pack))
    
    def Task4():
        root = Tk()
        root.title('Pack布局')
        App(root)
        root.mainloop()
        
    def Task5():
        root=Tk()
        root.title('Grid布局')
        Apps(root)
        root.mainloop()
        
    def Task6():
        root = Tk()
        root.title('place布局')
        root.geometry('250x250+30+30')
        App2(root)
        root.mainloop()
# =============================================================================
# 
# =============================================================================
class App3:
    def __init__(self,master):
        self.master = master
        self.initWidgets()
    def initWidgets(self):
        self.label = Label(self.master,text='Nothing',width=30)
        self.label['font'] = ('Courier',20)
        self.label['bg'] = 'white'
        self.label.pack()
        #简单的事件处理可以通过command选项来绑定
        bn = Button(self.master,text = '点击我',command=self.change)
        bn.pack()
    def change(self):
        self.label['text'] = '欢迎学习python'
        ct = [random.randrange(256) for x in range(3)]
        greyness = int(round(0.299*ct[0]+0.527*ct[1]+0.114*ct[2]))
        bg_color = '#%02x%02x%02x'%tuple(ct)  
        self.label['bg'] = bg_color
        self.label['fg'] = 'black' if greyness>125 else 'white'

class App4:
    def __init__(self, master):
        self.master = master
        self.initWidgets()
    def initWidgets(self):
        self.show = Label(self.master,width=30,bg='white',font = ('times',20))
        self.show.pack()
        bn = Button(self.master,text = '单击我或双击我')
        bn.pack(fill = BOTH,expand=YES)
        bn.bind('<Button-1>',self.one)
        bn.bind('<Double-1>',self.two)
    #event参数代表了传给该事件处理方法的实践对象
    def one(self,event):
        self.show['text'] = '左键单击:%s'%event.widget['text']
    def two(self,event):
        print('左键双击，退出程序:',event.widget['text'])
        import sys; sys.exit(0)

class App5:
    def __init__(self,master):
        self.master = master
        self.initWidgets()
    def initWidgets(self):
        lb = Label(self.master,width = 40,height=3)
        lb.config(bg='lightgreen',font=('Times',20))
        lb.bind('<Motion>',self.motion)
        lb.bind('<B1-Motion>',self.press_motion)
        lb.pack()
        self.show = Label(self.master,width=38,height=1)
        self.show.config(bg='white',font=('Courier',20))
        self.show.pack()
    def motion(self,event):
        #鼠标对于当前组件的位置可以通过event对象中的x和y属性来获得
        self.show['text'] = '鼠标移动到: (%s %s)'%(event.x,event.y)
        return
    def press_motion(self,event):
        self.show['text'] = '按住鼠标的当前位置为: (%s %s)'%(event.x,event.y)
        return

class App6:
    def __init__(self,master):
        self.master = master
        self.initWidgets()
        self.expr = None #表达式
    def initWidgets(self):
        self.display = Label(font=('Times',18),width=20,bg='white',anchor=NW)
        self.display.pack(side=TOP,pady=5)
        self.show = Label(relief=SUNKEN,font = ('Courier',24),\
                          width=25,bg='white',anchor = E)
        self.show.pack(side=TOP,pady=7)
        p=Frame(self.master)
        p.pack(side=TOP)
        names=('0','1','2','3','4','5','6','7','8','9','+','-','*','/','.','=')
        for i in range(len(names)):
            b = Button(p,text=names[i],font=('Verdana',20),width=6)
            b.grid(row=i//4,column=i%4)
            b.bind('<Button-1>',self.click)
            if b['text'] == '=':b.bind('<Double-1>',self.clean)
    def click(self,event):
        if event.widget['text'] in ('0','1','2','3','4','5',\
                       '6','7','8','9','.'):
            self.show['text'] += event.widget['text']
            self.display['text'] += event.widget['text']
        elif event.widget['text'] in ('+','-','*','/'):
            if self.expr == None:
                self.expr = self.show['text'] + event.widget['text']
            else:
                self.expr += self.show['text'] + event.widget['text']
            self.show['text'] = ''
            self.display['text'] +=event.widget['text']
        elif event.widget['text'] =='=' and self.expr is not None:
            self.expr+=self.show['text']
            print(self.expr)
            #eval函数计算字符串表达式的值
            self.show['text'] = str(eval(self.expr))
            self.expr = None
    def clean(self,event):
            self.expr = None
            self.show['text'] = ''
            self.display['text'] = ''
            
def Chapter11_2():
    #事件处理     
    def Task1():
        root = Tk()
        root.title('简单事件处理')
        App3(root)
        root.mainloop()
    
    def Task2():
        root = Tk()
        root.title('简单绑定')
        App4(root)
        root.mainloop()
    
    def Task3():
        root = Tk()
        root.title('鼠标事件')
        App5(root)
        root.mainloop()
    
    def Task4():
        root = Tk()
        root.title('计算器')
        App6(root)
        root.mainloop()
# =============================================================================
#   
# =============================================================================
from tkinter import ttk

def Chapter11_3():
    
    pass
# =============================================================================
# 
# =============================================================================
from pathlib import *
def Chapter12_1(): #文件IO
    def Task1():
        pp = PurePath('desktop','setup.py')
        print(type(pp),pp,sep='\n')
        pp = PurePath('crazyit','some/path','info') #windows
        print(pp)
        pp = PurePosixPath('crazyit','some/path','info') #linux
        print(pp)
        pp = PurePath()
        print(pp) #不传入参数则代表当前路径'.
        pp = PurePath('/etc','/usr','lib')
        print(pp) #传入的参数包含多个根路径时，只有最后一个根路径及后面的子路径生效
        pp = PurePath('c:/windows','d:info')
        print(pp)
        pp = PurePath('c:/windows','/Program Files') #windows下只有盘符才能算根路径
        print(pp)
        pp = PurePath('foo/./bar','com')
        print(pp) #路径字符串中包含多余的斜杠和点号，系统会直接忽略它们
        #windows风格下，路径不区分大小写；linux风格下反之
        print(PureWindowsPath('d:windows') == PureWindowsPath('D:windows'))
        print(PurePosixPath('d:windows')==PurePosixPath('D:windows'))
        #不同风格下的路径字符串可以比较是否相等，但不能比较大小，否则会引发错误
        print(PureWindowsPath('d:windows')==PurePosixPath('d:windows')) #永远为false
        pp = PurePath('abc')
        print(pp/'cde'/'fgh') #斜线'/'用于将对各类眼镜连接起来
        pp2 = PurePath('lib')
        print(pp/pp2)
        print(str(pp/pp2)) #windows使用反斜杠作为分隔符
        
    def Task2(): #PurePath的属性和方法
        #parts属性返回路径字符串所包含的各部分
        print(PureWindowsPath('c:/Program Files/').parts)
        print(PureWindowsPath('../Program Files/').parts)
        #drive属性返回路径字符串中的驱动器盘符
        print(PureWindowsPath('c:/Program Files/').drive)
        print(PureWindowsPath('/Program Files/').drive)
        #root属性返回路径字符串中的根路径
        print(PureWindowsPath('c:/Program Files/').root) #'\'表示根目录
        print(PurePosixPath('/Program Files/').root) #'/'表示根目录
        #anchor属性返回盘符和根路径
        print(PureWindowsPath('c:/Program Files/').anchor)
        print(PurePosixPath('/Program Files/').anchor)
        #parents属性返回当前路径的全部父路径
        p = PurePath('abc/xyz/wawa/haha')
        print(p.parents[0])
        print(p.parents[1])
        print(p.parents[3]) #当前路径
        #parent属性返回当前路径的上一级路径
        print(p.parent)
        #name属性返回当前路径中的文件名
        print(p.name)
        p=PurePath('windows/abc.txt')
        print(p.name)
        #suffixes属性返回当前路径中的文件所有后缀名
        p = PurePath('abc/wawa/bb.txt.tar.zip')
        print(p.suffixes[0])
        print(p.suffixes[2])
        #suffix属性返回当前路径中的文件后缀名
        print(p.suffix) #相当于suffixes属性返回的列表的最后一个元素
        #stem属性返回当前路径中的主文件名
        print(p.stem)
        #as_posix()将当前路径转换成linux风格的路径
        p = PurePath('abc','def','ghi','jkl')
        print(p)
        print(p.as_posix())
        #as_uri()将绝对路径转换为URI
        p = PurePath('d:/','windows','lib')
        print(p.as_uri())
        #is_absolute()判断是否为绝对路径
        print(p.is_absolute())
        #joinpath()将多个路径连接在一起
        print(p.joinpath('abc'))
        #match()判断当前路径是否匹配制定通配符
        print(PurePath('a/b.py').match('*.py'))
        print(PurePath('a/b/c.py').match('b/*.py'))
        print(PurePath('a.b.c.py').match('a/*.py'))
        #relative_to()获取当前路径中去除基准路径之后的结果
        p = PurePosixPath('c:/abc/xyz/wawa')
        print(p.relative_to('c:'))
        print(p.relative_to('c:/abc'))
        #with_name()将当前路径中的文件名替换成新的文件名;若没有文件名则会引发ValueError
        p = PureWindowsPath('e:/Downloads/pathlib.tar.gz')
        print(p.with_name('fkit.py'))
        #with_suffix()将当前路径中的文件后缀名替换成新的后缀名；如果没有后缀名，则会添加新的后缀名
        print(p.with_suffix('.zip'))
        print(PurePath('README').with_suffix('.txt'))
    
    def Task3(): #Path时PurePath的子类，Path会真正访问底层的文件路径
        #iterdir()返回Path对应目录下的所有子目录和文件
        p = Path('.')
        for x in p.iterdir():
            print(x)
        p = Path('../')
        for x in p.glob('**/*.py'):
            print(x)
        p = Path('test.txt')
        #write_text()用于输出文本数据到Path对应文件
        result = p.write_text('''有一个美丽的世界
                              它在远方等我''',encoding='GBK')
        print(result)
        #read_text()用于读取Path对应文件的文本数据
        content = p.read_text(encoding='GBK')
        print(content)
        print(p.read_bytes())
    
    Task3()
    
if __name__=='__main__':
        Chapter12_1()
        
        
        
        
        
        
        
        
        