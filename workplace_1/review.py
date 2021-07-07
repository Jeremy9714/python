# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 19:43:54 2020

@author: Chenyang
"""
from urllib.parse import *
from urllib.request import *

def Chapter15_1():
    result = urlparse('http://www.crazyit.org:80/index.php;yeeku?name=fkit#frag')
    print(result)
    print('scheme:', result.scheme,result[0])
    print('主机和端口:', result.netloc,result[1])
    print('主机:', result.hostname)
    print('端口', result.port)
    print('资源路径', result.path,result[2])
    print('参数', result.params,result[3])
    print('查询字符串', result.query,result[4])
    print('fragments', result.fragment,result[5])
    print(result.geturl())
    print(urlunparse(result)) #将ParseResult对象或元组恢复成URL字符串
    result = urlunparse(('http','www.baidu.com:250','wwe.php',
                         'jeremy','name=fkit','frag'))
    print(result)
    result = urlparse('//www.crazyit.org:80/index.php') #被解析的URL以双斜线开头，则可以识别出主机，只是缺少scheme
    print('scheme:',result.scheme,result[0])
    print('主机和端口:',result.netloc,result[1])
    print('资源路径:',result.path,result[2])
    print(result)

    result = urlparse('www.crazyit.org:80/index.php') #若被解析的URL也没有以双斜线开头，则urlparse()将会把这些URL都当成资源路径
    print('scheme:',result.scheme,result[0])
    print('主机和端口:', result.netloc)
    print('资源路径:',result.path)
    print(result,'\n')

    result = parse_qs('name=fkit&name=%22%23%24java&age=23')
    print(result) 
    result = parse_qsl('name=fkit&name=%22%23%24java&age=23')
    print(result)
    print(urlencode(result)) #将请求参数恢复成请求字符串
    print()
    

    result = urljoin('http://www.crazyit.org/users/login.html','book/help.html')
    print(result) #如果被拼接的URL只是一个相对路径，则该URL将会被拼接到base之后，替换base中的path部分
    result = urljoin('http://www.crazyit.org/users/login.html','/help.html')
    print(result)
    result = urljoin('http://www.crazyit.org/users/login.html','//help.html')
    print(result)
    print()
    
    result = urlopen('https://fkjava.org/2019/04/01/python')
    data = result.read(326)
    print(data.decode('utf-8'))
    
    
    


if __name__ == '__main__':
    Chapter15_1()