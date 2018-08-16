# -*- coding: utf-8 -*-
"""
@Time    : 2018/8/15 下午2:18
@Author  : libing
@Email   : icearl@qq.com
@File    : 48_不用加减乘除做加法.py
@Software: PyCharm
"""

"""
写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。
"""

# -*- coding:utf-8 -*-
class Solution:
    def Add(self, num1, num2):
        # write code here
        s=[]
        s.append(num1)
        s.append(num2)
        return sum(s)