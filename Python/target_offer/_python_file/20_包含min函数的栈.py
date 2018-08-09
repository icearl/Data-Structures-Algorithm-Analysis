'''
书：21 题
定义栈的数据结构，请在该类型中实现一个能够得到栈最小元素的min函数。
'''

"""
思路：
一个存储数值的栈 val
另外维护一个最小值组成的栈 min
当 val 为空的时候，直接把当前的 node 加到 min 栈上，否则比较一下当前 min 和当前 node，把小的加到 min 上
"""

# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack_val = []
        self.stack_min = []

    def push(self, node):
        if self.stack_val == []:
            self.stack_min.append(node)
        else:
            if self.min() > node:
                self.stack_min.append(node)
            else:
                self.stack_min.append(self.min())
        self.stack_val.append(node)

    def pop(self):
        if self.stack_val == [] or self.stack_min == []:
            return None
        a = self.stack_val.pop()
        self.stack_min.pop()
        return a

    def top(self):
        return self.stack_val[-1]

    def min(self):
        return self.stack_min[-1]

S = Solution()
S.push(3)
S.push(4)
S.push(2)
S.push(1)
print(S.min())
S.pop()
print(S.min())
S.pop()
print(S.min())