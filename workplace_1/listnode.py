# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 12:27:05 2020

@author: Chenyang
"""

class Node(object):
    
    def __init__(self, data, next = None):
        '''data为数据项 next为下一节点的链接 初始化节点默认链接为None'''
        self.data = data
        self.next = next
        
node1 = None
node2 = Node(1, None)
node3 = Node('hello', node2)
print(node1, node2.next, node2, node3.next)