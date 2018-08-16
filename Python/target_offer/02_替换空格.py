"""
题目：书 5
请实现一个函数，将一个字符串中的空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
"""

# 本题思路：
# python 基本操作：注意 python 中的 string 是不可变对象

# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replace_space(self, s):
        s_list = list(s)  # str 是不可变对象，要用 list 方法变成可变对象
        for i in range(len(s_list)):
            if s_list[i] == ' ':
                s_list[i] = '%20'
        return ''.join(s)   # 这里将S又变回字符串