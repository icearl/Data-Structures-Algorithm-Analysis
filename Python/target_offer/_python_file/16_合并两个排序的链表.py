'''
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
'''

"""
思路：
1. 按小的往里合
2. 剩下的直接接后面就可以
注意：merge 链表，初始化的时候，可以用 nil 来简化操作（不用考虑p_head1 or p_head2 第一个节点是否为 None）
"""

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

    def Merge(self, pHead1, pHead2):
        """
        循环法
        :param pHead1:
        :param pHead2:
        :return:
        """
        p_head1 = pHead1
        p_head2 = pHead2
        if p_head1 is None:
            return p_head2
        if p_head2 is None:
            return p_head1

        p_cur = nil = ListNode(-1)

        while p_head1 is not None and p_head2 is not None:
            if p_head1.val <= p_head2.val:
                p_cur.next = p_head1
                p_head1 = p_head1.next
            else:
                p_cur.next = p_head2
                p_head2 = p_head2.next
            p_cur = p_cur.next

        if p_head1 is not None:
            p_cur.next = p_head1
        if p_head2 is not None:
            p_cur.next = p_head2

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
merge = S.Merge(node1, node4)
while merge is not None:
    print(merge.val)
    merge = merge.next