# -*- coding:utf-8 -*-
"""
用两个栈实现队列：书 9
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