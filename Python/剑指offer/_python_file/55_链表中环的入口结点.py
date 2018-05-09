'''
一个链表中包含环，请找出该链表的环的入口结点。
'''

"""
https://blog.csdn.net/shansusu/article/details/50285735
http://www.cnblogs.com/snake-hand/p/3148328.html
http://bookshadow.com/weblog/2015/07/10/leetcode-linked-list-cycle-ii/
"""

# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        if pHead == None or pHead.next == None or pHead.next.next == None:
            return None
        nil = ListNode(-1)
        nil.next= pHead
        low = nil.next
        fast = nil.next.next
        while low != fast:
            if fast.next == None or fast.next.next == None:
                return None
            # 慢指针每次走一步
            low = low.next
            # 快指针每次走两步
            fast = fast.next.next
        # 如果题目问的是链表有没有坏，则在这里判断。如果快指针先走到了一个null值，则无环;如果快慢指针相遇了，则有环。
        low = nil  # 当快慢指针相遇之后，将快指针放回至头结点
        while low != fast:  # 快指针和慢指针每次各走一步
            low = low.next
            fast = fast.next
        return low  # 最后相遇点就是环的入口点

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node3

s = Solution()
print(s.EntryNodeOfLoop(node1).val)