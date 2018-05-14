"""
输入两个链表，找出它们的第一个公共结点。
"""


# 暴力遍历法O(mn)：
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindFirstCommonNode(self, head1, head2):
        # write code here
        list1 = []
        list2 = []
        node1 = head1
        node2 = head2
        while node1:
            list1.append(node1.val)
            node1 = node1.next
        while node2:
            if node2.val in list1:
                return node2
            else:
                node2 = node2.next

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        """
        思路：
        一定是 Y 型的，后面的一定一样
        用快慢指针
        :param pHead1:
        :param pHead2:
        :return:
        """
        nLength1 = self.GetListLength(pHead1)
        nLength2 = self.GetListLength(pHead2)
        nLengthDiff = abs(nLength1 - nLength2)

        if nLength1 > nLength2:
            pListHeadLong = pHead1
            pListHeadShort = pHead2
        else:
            pListHeadLong = pHead2
            pListHeadShort = pHead1

        for i in range(nLengthDiff):
            pListHeadLong = pListHeadLong.next

        while pListHeadLong != None and pListHeadShort != None and pListHeadLong != pListHeadShort:
            pListHeadLong = pListHeadLong.next
            pListHeadShort = pListHeadShort.next

        pFirstCommonNode = pListHeadLong
        return pFirstCommonNode

    def GetListLength(self, pHead):
        nLength = 0
        while pHead != None:
            pHead = pHead.next
            nLength += 1
        return nLength