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
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        # write code here
        self.stack1.append(node)

    def pop(self):
        # return xx
        if self.stack2 == []:
            while self.stack1 != []:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
