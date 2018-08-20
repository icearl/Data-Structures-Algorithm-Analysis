# -*- coding: utf-8 -*-
"""
@Time    : 2018/8/15 下午5:07
@Author  : libing
@Email   : icearl@qq.com
@File    : 57_二叉树的下一个节点.py
@Software: PyCharm
"""

"""书：8
题：
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
"""

"""
1、 先找右节点，有的话，找到右节点最左边的那个
2、 找父节点
    1、 如果是父节点的左儿子，直接返回父亲节点
    2、 若为右儿子，一直往上找，知道找到是父亲的左儿子的那个节点，返回之
"""

# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None #.next属性代表当前节点的父节点
class Solution:
    def GetNext(self, pNode):
        # write code here
        if not pNode:
            return pNode
        if pNode.right is not None:
            left1 = pNode.right
            while left1.left is not None:
                left1 = left1.left
            return left1
        while pNode.next is not None:  # pNode节点的父节点
            tmp = pNode.next
            if tmp.left == pNode:
                return tmp
            pNode = tmp
