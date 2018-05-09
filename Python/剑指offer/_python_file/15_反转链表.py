"""
反转链表
输入一个链表，反转链表后，输出链表的所有元素
"""


# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def ReverseList(self, pHead):
        """
        循环法:前插法
        """
        if pHead is None or pHead.next is None:  # 如果链表是空或者链表只有一个节点
            return pHead
        pNode = pHead
        pPrev = None
        while pNode is not None:
            pNext = pNode.next
            pNode.next = pPrev

            pPrev = pNode
            pNode = pNext
        return pPrev

    # 递归实现反转链表
    def ReverseListRec(self, pHead):
        """
        递归法
        """
        # 基本情况
        if pHead is None or pHead.next is None:  # 如果链表是空或者链表只有一个节点
            return pHead
        # 递归情况
        else:
            pReversedHead = self.ReverseList(pHead.next)
            pHead.next.next = pHead
            pHead.next = None
            return pReversedHead


node1 = ListNode(10)
node2 = ListNode(11)
node3 = ListNode(13)
node1.next = node2
node2.next = node3

S = Solution()
p = S.ReverseList(node1)
print(p.next.val)
