"""" 书 23
一个链表中包含环，请找出该链表的环的入口结点。
"""

"""
https://blog.csdn.net/shansusu/article/details/50285735
http://bookshadow.com/weblog/2015/07/10/leetcode-linked-list-cycle-ii/
"""

# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        if pHead is None or pHead.next is None:
            return None
        # 从 pHead 出发
        p_fast, p_slow = pHead.next.next, pHead.next
        while p_fast != p_slow:
            # 判断是否有环
            # if p_fast == None or fast.next == None:
            #     return None
            p_fast = p_fast.next.next
            p_slow = p_slow.next
        # 如果题目问的是链表有没有坏，则在这里判断。如果快指针先走到了一个null值，则无环;如果快慢指针相遇了，则有环。
        p_meet = p_fast
        # 也要从 pHead 出发
        p_start = pHead
        while p_meet != p_start:
            p_meet = p_meet.next
            p_start = p_start.next
        return p_meet

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