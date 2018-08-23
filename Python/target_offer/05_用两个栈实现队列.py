# -*- coding:utf-8 -*-
"""书 9
用两个栈实现队列：
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
"""

"""
一般思路：
1. 具体例子
2. 画图形象化
3. 时刻记得问题

本题思路：
入队：将元素进栈A
出队：
    判断栈B是否为空，
        如果为空，则将栈A中所有元素pop，并push进栈B，栈B出栈； 
        如果不为空，栈B直接出栈。
"""

class Solution:
    def __init__(self):
        self.in_stack = []
        self.out = []
    def push(self, node):
        # write code here
        self.in_stack.append(node)
    def pop(self):
        # return xx
        if self.out == []:
            while self.in_stack != []:
                self.out.append(self.in_stack.pop())
        return self.out.pop()


P = Solution()
P.push(10)
P.push(11)
P.push(12)
print(P.pop())
P.push(13)
print(P.pop())
print(P.pop())
print(P.pop())
print(P.pop())

"""书：9
另一个题,用两个队列实现一个栈
"""

"""
思路：
 push：新来的先放到非空的那个队列队尾
 pop：非空的队列1 把前面 n - 1 放到另一个队列里，剩下的那个弹出就好
"""

class Solution:

    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, x):
        # 哪个
        if self.queue2 == []:
            self.queue1.append(x)
        else:
            self.queue2.append(x)
    def pop(self):
        if not self.queue1 and not self.queue2:
            return
        if self.queue1 != []:
            length = len(self.queue1)
            for i in range(length-1):
                self.queue2.append(self.queue1.pop(0))
            return self.queue1.pop()
        else:
            length = len(self.queue2)
            for i in range(length-1):
                self.queue1.append(self.queue2.pop(0))
            return self.queue2.pop()

P = Solution()
P.push(10)
P.push(11)
P.push(12)
print(P.pop())
P.push(13)
print(P.pop())
print(P.pop())
print(P.pop())
print(P.pop())