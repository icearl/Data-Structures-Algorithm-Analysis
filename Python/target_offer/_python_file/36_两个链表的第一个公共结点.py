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
        len_1 = self.linklist_len(pHead1)
        len_2 = self.linklist_len(pHead2)
        sub_len = abs(len_1 - len_2)

        p_node1 = pHead1
        p_node2 = pHead2
        # 长的先把长的那一段走完
        if len_1 >= len_2:
            for i in range(sub_len):
                p_node1 = p_node1.next
        else:
            for i in range(sub_len):
                p_node2 = p_node2.next

        while p_node1 is not None:
            if p_node1.val == p_node2.val:
                return p_node1
            p_node1 = p_node1.next
            p_node2 = p_node2.next
        return None

    def linklist_len(self, pHead):
        nLength = 0
        while pHead != None:
            pHead = pHead.next
            nLength += 1
        return nLength
