# 和书上的类似，只是不用链表，也不用每次循环 m 次了
# -*- coding:utf-8 -*-
class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if not m or not n:
            return -1
        res = range(n) #res最开始的取值是完整的环的人数，将其看成每次循环的进制
        i = 0
        while len(res)>1:
            i = (i+m-1)%len(res)
            res.pop(i)
        return res[0]