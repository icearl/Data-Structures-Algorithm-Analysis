# 队列的特点是「先进先出」，一般有这几个操作

# enqueue 将一个元素存入队列中
# dequeue 将一个元素从队列中取出，并在队列中删除它

# empty 查看栈是否是空的

# 可以把队列看做排队，银行叫号机就是队列，先取号的先入队，叫号的时候也就先出队


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)