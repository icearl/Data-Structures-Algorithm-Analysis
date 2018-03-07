class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(3)
a4 = ListNode(4)
a5 = ListNode(5)
a6 = ListNode(6)

b1 = ListNode(4)
b2 = ListNode(5)

a1.next = a2
a2.next = a3
a3.next = a4
a4.next = a5
a5.next = a6

b1.next = b2
