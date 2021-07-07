# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 20:33:24 2020

@author: Chenyang
"""
from tkinter import *
class StringSeq:
    def __init__(self):
        self.mylist={}
    def __len__(self):
        print("function len called")
        return 20**2
    def __setitem__(self, key, value):
        print("function setitem called")
        self.mylist[key] = value
    def __getitem__(self,key):
        print("function getitem called")
        if key in self.mylist:
            return self.mylist[key]
        else:
            return None
    def __delitem__(self,key):
        print("function delitem called")
        if key in self.mylist:
            del self.mylist[key]

c = StringSeq()
print(len(c))       
c['a'] = 20  
print(c['a'])
del c['a']

class Fibs:
    def __init__(self, len):
        self.first = 0
        self.second = 1
        self.__len = len
    def __iter__(self):
        return self
    def __next__(self):
        if self.__len == 0:
            raise StopIteration("done")
        self.first, self.second = self.second, self.first+self.second
        self.__len-=1
        return self.first

f = Fibs(10)
print(next(f))
for el in f:
    print(el,end=' ')
print() 
def test(val, step):
    cur = 0
    for i in range(val):
        cur+=i*step
        yield cur
t = test(10,2)
print(tuple(t))

def gen(val):
    i=0
    out_val=0
    while i<val:
        out_val = (yield out_val**2) if out_val is not None else (yield i**2)
        if out_val is not None:print(out_val)
        i+=1
        
g = gen(5)
print(next(g))
print(g.send(20))
#g.throw(ValueError("nothing"))
#g.close()
print(next(g))

class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.initWidgets()
    def initWidgets(self):
        w = Label(self)
        bw = PhotoImage(file='images\\timg.png')
        w.x = bw
        w['image'] = bw
        w.pack()
        okButton = Button(self,text='确定')
        okButton['background'] = 'yellow'
        okButton.pack()
print()
app = Application()
app.master.title('窗口标题')
app.mainloop()