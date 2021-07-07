# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 20:25:58 2020

@author: Chenyang
"""
from pathlib import *
import sys
import os
import time
import random
import re
import fnmatch
import fileinput
import linecache
import stat
import tempfile
import threading

def Part1():
    pp = PurePath('setup.py')
    print(type(pp))
    pp = PurePath('crazyit', 'some/path', 'info')
    print(pp, type(pp))
    pp = PurePath(Path('crazyit'), Path('info'))
    print(pp)
    pp = PurePosixPath('crazyit', 'some/path', 'info')
    print(type(pp), pp, sep = '|')
    pp = PurePath()
    print(pp)
    pp = PurePosixPath('/etc', '/usr', 'lib34')
    print(pp)
    pp = PureWindowsPath('C:/Windows', 'D:info')
    print(pp)
    pp = PureWindowsPath('c:Windows', '/Program Files')
    print(pp)
    pp = PurePath('foo/../bar')
    print(pp)
    print(PurePath('c:Windows') in {PureWindowsPath('C:Windows')})
    print(PurePosixPath('/crazyit')<PurePosixPath('/brazyit'))
    print(PurePath('info') == PurePath('INFO'))
    print(PureWindowsPath('crazyit') == PurePosixPath('crazyit'))
    print(PurePath('fkit')/'xyz'/'abc')
    print(str(pp))
    print()
    
    print(pp.parts)
    pp = PurePath('abc/xyz/wawa/haha')
    pp1 = PurePath('c:/Program Files/')
    pp2 = PurePath('c:Program Files/')
    pp3 = PurePosixPath('/etc')
    
    print(pp1.drive, pp2.drive, pp3.drive)
    print(pp1.root, pp2.root, pp3.root)
    print(pp1.anchor, pp2.anchor, pp3.anchor)
    print(pp.parents[0], pp.parents[1], pp.parents[2])
    print(pp.parent)
    print(pp.name)
    pp = PurePath('abc/xyz/tb.txt')
    print(pp.name)
    pp = PurePath('abc/xyz/bb.txt.zip.mp4')
    print(pp.suffixes[0],pp.suffixes[1], pp.suffixes[2])
    print(pp.suffix)
    print(pp.stem, pp.name) #文件名=主文件名加后缀名
    print(pp.as_posix())
    print(pp.is_absolute())
    pp = PurePath('D:/', 'crazyit', 'python3')
    print(pp.is_absolute())
    print(pp.as_uri())
    print(pp.joinpath(PurePath('fkit')))
    pp = PurePath('abc/xyz/wawa/haha')
    print(pp.relative_to('abc'),pp.relative_to('abc/xyz'))
    pp = PurePath('e:/Downloads/pathlib.tar.zip')
    print(pp.with_name('fkit.txt'))
    pp = PurePath('README')
    print(pp.with_suffix('.mp4.tar.mp3'))
    print()
    
    p = Path('.')
    for i in p.iterdir():
        print(i)
    p = Path('..')
    for i in p.glob('**/*.py'):
        print(i)
    p = Path('bored.txt')
    result = p.write_text('''第一行
                          第二行
                          第三行
                          最后一行''', encoding='GBK')
    print(result)
    content = p.read_text(encoding='GBK')
    print(content)
    bb = p.read_bytes()
    print(bb)
    
def Part2():
    print(os.path.abspath('bored.txt'))
    print(os.path.commonpath(['/usr/lib', '/usr/local/lib']))
    print(os.path.commonprefix(['/usr/lib', '/usr/local/lib']))
    print(os.path.dirname('abc/xyz/README.txt'))
    print(os.path.exists('abc/xyz/README.txt'))
    print(time.ctime(os.path.getatime('bored.txt')))
    print(time.ctime(os.path.getmtime('bored.txt')))
    print(time.ctime(os.path.getctime('bored.txt')))
    print(os.path.getsize('bored.txt'))
    print(os.path.isfile('bored.txt'))
    print(os.path.isdir('bored.txt'))
    print(os.path.samefile('bored.txt', './bored.txt'))
    print()
    
    for file in Path('.').iterdir():
        if fnmatch.fnmatch(file, '*_*.PY'):
            print(file)
    print(fnmatch.fnmatchcase('abc.py','*.PY'))
            
    names=['a.py','b.py','c.py','d.py']
    sub = fnmatch.filter(names,'[a-c].py')
    print(sub)
    print(fnmatch.translate('[a-c].py'))

def Part3():
    f = open('7_28.py')
    print(f.encoding)
    print(f.mode)
    print(f.name)
    print(f.closed)
    f = open('test.txt', 'r', True)
    try:
        while True:
            ch = f.read(1) #若不传入参数，则会读取全部参数
            if not ch: break
            print(ch, end='')
    finally:
        f.close()
    
    f = open('7_28.py','rb', True)
    print(f.read().decode('utf-8'))
    f.close()
    print()
    f = open('7_28.py','r', True, 'utf-8')
    try:
        while True:
            ch = f.read(1)
            if not ch: break
            print(ch, end='')
    finally:
        f.close()

def Part4():
    f = open('test.txt', 'r', True)
    while True:
        line = f.readline()
        if not line: break
        print(line, end='')
    f.close()
    
    f = open('7_28.py', 'r', True, 'utf-8')
    for l in f.readlines():
        print(l, end='')
    f.close()
    
    for line in fileinput.input(files=('1.txt','2.txt')):
        print(fileinput.filename(), fileinput.filelineno(), line, end='')
    fileinput.close()
    print()
    
    f = open('poem.txt', 'r', True, 'utf-8')
    for line in f:
        print(line, end='')
    f.close()
    print()
    
    print(list(open('test.txt', 'r', True)))
    for line in sys.stdin:
        print('用户输入:', line, end='')

def Part5():
    mailPattern = r'([a-z0-9]*[-_]?[a-z0-9]+)*@([a-z0-9]*[-_]?[a-z0-9]+)+'\
    + '[\.][a-z]{2,3}([\.][a-z]{2})?'
    text = sys.stdin.read()
    it = re.finditer(mailPattern, text, re.I)
    for e in it:
        print(str(e.span()) + '-->' + str(e.group()))

def Part6():
    with open('ad.txt', 'r', True, 'utf-8') as f:
        for line in f:
             print(line, end='')
    print()
    with fileinput.input(files=('1.txt', '2.txt')) as f:
        for line in f:
            print(line, end='')
    class FkResource:
        def __init__(self, tag):
            self.tag = tag
            print('构造器，初始化资源：%s'%tag)
        def __enter__(self):
            print('[__enter__ %s]: '%self.tag)
            return 'fkit'
        def __exit__(self, exc_type, exc_value, exc_traceback):
            print('[__exit__ %s]: '%self.tag)
            if exc_traceback is None:
                print('没有异常时关闭资源')
            else:
                print('遇到异常时关闭资源')
                return False
    
    with FkResource('孙悟空') as dr:
        print(dr)
        print('[with代码块]没有异常')
        print('----------------------------------')
    try:
        with FkResource('白骨精'):
            print('[with代码块]异常之前的代码')
            raise Exception
            print('[with代码块]异常之后的代码')
    except Exception:
        print('error occured')

def Part7():
    print(linecache.getline(random.__file__, 3))
    print(linecache.getline('7_28.py',1))
    linecache.clearcache()
    print(linecache.checkcache())
    
    f = open('test.txt', 'rb')
    print(f.tell())
    f.seek(-3, 2)
    print(f.tell(), type(f.read(1)))
    f = open('7_28.py', 'r', True, 'utf-8')
    f.seek(400, 0)
    print(type(f.read(1)))
    
    f = open('test.txt', 'w+')
    f.write('我爱python' + os.linesep) #系统上的换行符
    f.writelines(('床前明月光' + os.linesep,
                  '疑似地上霜' + os.linesep,
                  '举头望明月' + os.linesep,
                  '低头思故乡' + os.linesep))
    f = open('1.txt', 'wb+')
    f.write(('我爱python' + os.linesep).encode('utf-8'))
    f.writelines((('床前明月光' + os.linesep).encode('utf-8'),
                  ('疑似地上霜' + os.linesep).encode('utf-8'),
                  ('举头望明月' + os.linesep).encode('utf-8'),
                  ('低头思故乡' + os.linesep).encode('utf-8')))
    
def Part8():
    print(os.getcwd())
    os.chdir('images')    
    print(os.getcwd())
    path = 'my_dir'
    os.mkdir(path, 0o755)
    path = 'abc/def/ghi'
    os.makedirs(path, 0o755)
    print(os.listdir(path))
    path = 'my_dir'
    os.rmdir(path)
    path = 'abc/def/ghi'
    os.removedirs(path)
    os.chdir('..')
    print(os.getcwd())
    
    path = 'my_dir'
    os.mkdir(path, 0o755)
    os.rename(path, 'your_dir')
    os.rmdir('your_dir')
    path = 'abc/def/ghi'
    os.makedirs(path, 0o755)
    os.renames(path, 'xyz/uvw/rst')
    os.removedirs('xyz/uvw/rst')
    
    ret = os.access('.',os.F_OK|os.R_OK|os.W_OK|os.X_OK)
    print(ret)
    os.chmod('os.txt', stat.S_IREAD)
    ret = os.access('os.txt',os.F_OK|os.R_OK|os.W_OK)
    print(ret)
    
def Part9():
    f = os.open('dude.txt',os.O_RDWR|os.O_CREAT)
    len1 = os.write(f, '我自横刀向天笑, \n'.encode('utf-8'))
    len2 = os.write(f, '去留肝胆两昆仑. \n'.encode('utf-8'))
    os.lseek(f,0,os.SEEK_SET)
    data = os.read(f, len1+len2)
    print(data.decode('utf-8'))
    os.close(f)
    print(os.access('dude.txt',os.F_OK|os.R_OK|os.W_OK|os.X_OK))
    os.chmod('dude.txt',stat.S_IWRITE)
    print(os.access('dude.txt',os.W_OK))
    
    #os.symlink('7_28.py','tt')
    #os.link('7_28.py','dst')
    print()
    
    fp = tempfile.TemporaryFile()
    print(fp.name)
    fp.write('两情若是久长时,'.encode('utf-8'))
    fp.write('又岂在朝朝暮暮.'.encode('utf-8'))
    fp.seek(0)
    print(fp.read().decode('utf-8'))
    fp.close()
    
    with tempfile.TemporaryFile() as fp:
        fp.write(b'I Love Python')
        fp.seek(0);
        print(fp.read())
    with tempfile.TemporaryDirectory() as tmpdirname:
        print('创建临时目录', tmpdirname)
    
def Part10(): #sql数据库
    import sqlite3
    print(sqlite3.apilevel, sqlite3.paramstyle)
    conn = sqlite3.connect('first.db')
    c = conn.cursor()
    c.execute('''create table user_tb(
            _id integer primary key autoincrement,
            name text,
            pass text,
            gender text)''')
    c.execute('''create table order_tb(
            _id integer primary key autoincrement,
            item_name text,
            item_price real,
            item_number real,
            user_id integer,
            foreign key(user_id) references user_tb(_id) )''')
    c.close()
    conn.close()

def Part11(): #通过使用threading模块的Thread类的构造器创建线程
    def action(max):
        for i in range(max):
            print(threading.current_thread().getName() + " " + str(i))
    for i in range(100):
        print(threading.current_thread().getName() + " " + str(i))
        if i == 20:
            t1 = threading.Thread(target=action, args=(100,))
            t1.start()
            t2 = threading.Thread(target=action, args=(100,))
            t2.start()
    print('--------------主线程执行完成----------------')

class FkThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.i = 0
    def run(self):
        while self.i < 100:
            print(threading.current_thread().getName() + " " + str(self.i))
            self.i += 1
            
def Part12(): #通过继承threading模块的Thread类创建线程类
    for i in range(100):
        print(threading.current_thread().getName() + " " + str(i))
        if i == 20:
            ft1 = FkThread()
            ft1.start()
            ft2 = FkThread()
            ft2.start()
    print('----------------主线程执行完毕---------------')

def action(max):
    for i in range(max):
        print(threading.current_thread().name + " " + str(i))
        
def Part13():
    for i in range(100):
        print(threading.current_thread().name + " " + str(i))
        if i == 20:
            threading.Thread(target=action, args=(100,)).run()
            threading.Thread(target=action, args=(100,)).run()
            
def Part14():
    threading.Thread(target=action,args=(100,), name='新线程').start()
    for i in range(100):
        if i == 20:
            jt = threading.Thread(target=action, args=(100,), name='被join的线程')
            jt.start()
            jt.join(timeout=1000)
        print(threading.current_thread().name + " " + str(i))
            
    
    
    
if __name__ == '__main__':
    Part14()
