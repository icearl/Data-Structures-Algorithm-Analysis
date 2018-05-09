'''
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def Merge(self, pHead1, pHead2):
        """
        递归法
        """
        if pHead1 == None:
            return pHead2
        elif pHead2 == None:
            return pHead1

        pMergedHead = None
        if pHead1.val < pHead2.val:
            pMergedHead = pHead1
            pMergedHead.next = self.Merge(pHead1.next, pHead2)
        else:
            pMergedHead = pHead2
            pMergedHead.next = self.Merge(pHead1, pHead2.next)

        return pMergedHead

    def Merge(pHead1, pHead2):
        """
        循环法
        """
        nil = ListNode(-1)
        p = nil
        p1 = pHead1
        p2 = pHead2
        while p1 is not None and p2 is not None:
            if p1.val <= p2.val:
                p.next = p1
                p1 = p1.next
            else:
                p.next = p2
                p2 = p2.next
            p = p.next
        if p1 is not None:
            p.next = p1
        elif p2 is not None:
            p.next = p2
        return nil.next


node1 = ListNode(1)
node2 = ListNode(3)
node3 = ListNode(5)
node1.next = node2
node2.next = node3

node4 = ListNode(2)
node5 = ListNode(4)
node6 = ListNode(6)
node4.next = node5
node5.next = node6

S = Solution()
S.Merge(node1, node4)
print(node4.next.val)