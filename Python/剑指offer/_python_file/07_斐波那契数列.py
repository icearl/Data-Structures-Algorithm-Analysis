# -*- coding:utf-8 -*-
"""
大家都知道斐波那契数列(第三个数等于前两个数相加)，
现在要求输入一个整数n，请你输出斐波那契数列的第n项。n<=39
"""

"""
一般思路：
动态规划,把子问题保存下来。因为递归会有重复计算。

本体思路：
把递归思路转换成循环，减少重复计算。
"""

# 维护一个列表
class Solution:
    def Fibonacci(self, n):
        a = [0, 1, 1]
        if n < 3:
            return a[n]
        for i in range(3, n + 1):
            a.append(a[i - 1] + a[i - 2])
        return a[n]
# 更好的方案：维护前两个数
class Solution:
    def Fibonacci(self, n):
        re_list = [0, 1]
        if n < 2:
            return re_list[n]
        n_2 = 0
        n_1 = 1
        n_cur = 0
        for i in range(2, n + 1):
            n_cur = n_2 + n_1
            n_2 = n_1
            n_1 = n_cur
        return n_cur