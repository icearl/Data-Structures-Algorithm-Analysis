class Node:
    def __init__(self, val=-1):
        self.val = val
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None

    # O(1)
    def is_empty(self):
        return self.head is None

    # O(1)
    def add(self, item):
        temp = Node(item)
        temp.next = self.head
        self.head = temp

    # O(n)
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def find(self, element):
        node = self.head
        while node is not None:
            if node.element == element:
                break
            node = node.next
        return node