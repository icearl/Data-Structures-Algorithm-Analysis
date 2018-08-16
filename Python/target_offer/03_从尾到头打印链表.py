"""
题目：书 6
输入一个链表，从尾到头打印链表每个节点的值
"""

# 一般思路：
#

# 本题思路
# 思路一：允许改变结构 -> 先反转链表，然后逐个输出
# 思路二：
#   不允许改变结构 -> 用栈来存储
#   下面，没用栈，直接用列表l存储链表各个节点的.val属性，然后反向打印l

#-*- coding:utf-8 -*-
class ListNode:
     def __init__(self, x):#__init__()方法是一种特殊的方法，被称为类的构造函数或初始化方法，当创建了这个类的实例时就会调用该方法
         self.val = x
         self.next = None
#代表这个类的对象拥有.val和.next两个属性

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        p = listNode
        res = []
        while p is not None:
            # res中存储的是每个listNode节点.val属性的值
            res.append(p.val)
            # 这步将 p 每次更新到指向的下一个节点，到这步之后l是从头到尾的整个链表
            p = p.next
        # print l[::-1]
        return l[::-1]
