# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 10:18:35 2019

@author: Chenyang
"""
'''
class Animal(object):
    def __init__(self):
        self.info = 'this is an animal'
    def output(self, name, age, size):
        self.name = name
        self.age = age
        self.size = size
        print('%s, %d, %s' %(self.name, self.age, self.size))
        print(self.info)
        
class Dog(Animal):
    def __init__(self):
        super().__init__()
        print('this is a dog')
    def output(self, name, age, size):
        super().output(name, age, size)
    
class Cat(Animal):
    def __init__(self):
        super().__init__()
        print('this is a cat')
    def output(self, name, age, size):
        super().output(name, age, size)
    
class Pussy(Cat):
    def __init__(self):
        super().__init__()
        print('this is a pussy')
    def output(self, name, age, size):
        super().output(name, age, size)

p = Pussy()
d = Dog()
c = Cat()
p.output('tom', 6, 'big')
d.output('david', 10, 'medium')
c.output('jerry', 2, 'minor')
'''
'''
class Test(object):
    def __init__(self):
        self.l = [1,2,3,4,5,6]
        self.i = iter(self.l)
    def __call__(self):
        item = next(self.i)
        print('__call__ is called, which would return ', item)
        return item
    
t = Test()
t1 = iter(t, 3)
print(callable(t))
for i in t1:
    print(i)
'''
'''
class C(object):
    def __init__(self):
        self.x = None
 
    def getx(self):
        return self.x
 
    def setx(self, value):
        self.x = value
 
    def delx(self):
        del self.x
 
    x = property(getx, setx, delx, "I'm the 'x' property.")
'''
'''
a = frozenset({'a': 6, 'b': 7})
print(a)

a = {x for x in 'absdfacbgdgavbm' if x not in 'mads'}
print(a)

l = [1,2,3,4]
it = iter(l)
print(next(it))
'''
'''
import sys
 
def fibonacci(n): # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if counter > n: 
            return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(10) # f 是一个迭代器，由生成器返回生成
print(type(f))

while True:
    try:
        print (next(f), end=" ")
    except StopIteration:
        sys.exit()
'''
'''
def ChangeInt( a ):
    a = 10
 
b = 2
ChangeInt(b)
print( b ) # 结果是 2
'''
'''
l=lambda arg1, arg2, arg3: arg1 + arg2 - arg3
print(l(10,20,25))
'''
'''
l = [str(round(355/113, i)) for i in range(1,10)]
print(l)
'''
'''
import sys
sys.ps1 = 'C> '
print(sys.ps1)
'''
'''
while True:
    try:
        a = int(input('enter a number:'))
        break
    except ValueError as ve:
        print(ve)
        break
'''
'''
a = chr(int(input("a number:")))
print(ord(a))
'''
'''
from itertools import chain
a = [1,2,3]
b = ['a','aa','aaa', 'a2s']
c = [[1,2,3], ['a', 'b', 'c']]
print(list(chain(a,b)))
print(list(chain(*zip(a,b))))
print(list(chain(c)))
print(list(chain(*c)))
print(list(chain(*b)))
'''
'''
S = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
dic = {}
ans = []
for s in S:
    count, web = s.split()
    count = int(count)
    n = web.split(".")
    for j in range(len(n)):
        dic[".".join(n[j:])] = dic.get(".".join(n[j:]),0) + count
for i, j in dic.items():
    ans.append(' '.join([str(j), i]))
print(ans)
'''
'''
board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
Rx, Ry = 0, 0
ans = 0
for i in range(len(board)):
    for j in range(len(board[i])):
        if board[i][j] == 'R':
            Rx,Ry = i,j
xlist,ylist = board[Rx],[]
for i in range(len(board)):
    ylist.append(board[i][Ry])

for i in xlist[:]:
    if i =='.':
        xlist.remove(i)
for j in ylist[:]:
    if j == '.':
        ylist.remove(j)
Rx, Ry = xlist.index('R'), ylist.index('R')
if Rx -1 >= 0 and xlist[Rx-1] == 'p':
    ans+=1
if xlist[Rx+1] == 'p':
    ans+=1
if Ry - 1 >= 0 and ylist[Ry-1] == 'p':
    ans+=1
if ylist[Ry+1] == 'p':
    ans+=1
'''
'''
arr = [3,8,-10,23,19,-4,-14,27]
ans = []
a = sorted(arr)
prev = a[0]
print(prev)
Min = 99999
for i in range(1,len(a)):
    temp = abs(a[i]-prev)
    prev = a[i]
    print(prev)
    if temp <Min:
        Min = temp
        print("min is ", Min)
print(a)
for i in range(1,len(a)):
    if abs(a[i]-a[i-1]) == Min:
        ans.append([a[i-1],a[i]])
print(ans)
'''
'''
arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6,19]
arr2 += sorted(set(arr1)-set(arr2))
print(sorted(arr1,key=arr2.index))
'''
'''
nums = [[1,2],[3,4]]
a = [j for i in nums for j in i]
print(a)
'''
'''
nums1 = [4,1,2]
nums2 = [2,1,3,4]
stack, Hash = list(), dict()
for n in nums2:
    while stack and stack[-1]< n:
        Hash[stack.pop()] = n
        print(Hash)
        print(stack)
    stack.append(n)
    print(stack)
ans = [Hash.get(i, -1) for i in nums1] 
print(ans)
'''
