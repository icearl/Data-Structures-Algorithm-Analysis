# 栈的特点是「先进后出」，一般有这几个操作
# push 将一个元素存入栈中 O(1)
# pop  将一个元素从栈中取出，并在栈中删除它O(1)

# top  将一个元素从栈中取出
# is_empty 查看栈是否是空的

# size 栈的长度


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def top(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)