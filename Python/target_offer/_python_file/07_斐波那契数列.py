# -*- coding:utf-8 -*-
"""
大家都知道斐波那契数列(第三个数等于前两个数相加)，
现在要求输入一个整数n，请你输出斐波那契数列的第n项。n<=39
从第 0 项开始，第 0 项为0，第 1 项为 1
"""

"""
一般思路：
动态规划,把子问题保存下来。因为递归会有重复计算。

本体思路：
把递归思路转换成循环，减少重复计算。
"""

# 递归方法，很慢，正确但时间通不过
class Solution1:
    def Fibonacci(self, n):
        re_list = [0, 1]
        if n < 2:
            return re_list[n]
        else:
            cur = self.Fibonacci(n - 2) + self.Fibonacci(n - 1)
            return cur


# 维护一个列表
class Solution2:
    def Fibonacci(self, n):
        dp = [0, 1]
        if n < 2:
            return dp[n]
        for i in range(2, n + 1):
            cur = dp[i - 1] + dp[i - 2]
            dp.append(cur)
        return dp[n]
# 更好的方案：维护前两个数
class Solution3:
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

test = Solution1()
print(test.Fibonacci())