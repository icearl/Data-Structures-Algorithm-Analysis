# -*- coding: utf-8 -*-
"""
@Time    : 2018/8/15 下午3:55
@Author  : libing
@Email   : icearl@qq.com
@File    : 56_删除链表中重复的结点.py
@Software: PyCharm
"""

"""书：18-2
题：
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。 
例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
"""

# -*- coding:utf-8 -*-
# 方法一：递归解法
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if pHead is None or pHead.next is None:
            return pHead
        nexthead = pHead.next
        if nexthead.val != pHead.val:
            pHead.next = self.deleteDuplication(pHead.next)
        else:
            while pHead.val == nexthead.val and nexthead.next is not None:
                nexthead = nexthead.next
            if nexthead.val != pHead.val:
                pHead = self.deleteDuplication(nexthead)
            else:
                return None
        return pHead


# 方法二：循环解法(用这个）
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if pHead is None or pHead.next is None:
            return pHead
        nil = ListNode(-1)
        nil.next = pHead
        p = nil
        # 循环直到最后一个停下
        while p.next is not None and p.next.next is not None:
            if p.next.val == p.next.next.val:
                value = p.next.val
                while p.next is not None and p.next.val == value:
                    p.next = p.next.next
            else:
                p = p.next
        return nil.next

