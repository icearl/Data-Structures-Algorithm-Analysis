# -*- coding: utf-8 -*-
"""
@Time    : 2018/8/15 下午3:53
@Author  : libing
@Email   : icearl@qq.com
@File    : 54_字符流中第一个不重复的字符.py
@Software: PyCharm
"""

"""
题：
请实现一个函数用来找出字符流中第一个只出现一次的字符。
例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。
当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
输出描述:
如果当前字符流没有存在出现一次的字符，返回#字符。
"""

"""
思路：哈希 / 字典 记录次数就完事了
Insert也是要求定义的函数，起作用是改变self的.s和.dictionary属性的值
.dictionary用来统计单词出现的次数，存储形式为字典。
"""

# -*- coding:utf-8 -*-
class Solution:
    # 返回对应char
    def __init__(self):
        self.s = ''
        self.dictionary = {}

    def FirstAppearingOnce(self):
        # write code here
        for i in self.s:
            if self.dictionary[i] == 1:
                return i
        return '#'

    def Insert(self, char):
        # write code here
        self.s = self.s + char
        if char in self.dictionary:
            self.dictionary[char] = self.dictionary[char] + 1
        else:
            self.dictionary[char] = 1

        '''
        上面 4 行的另一种写法：
        if char not in self.dictionary:
            self.dictionary[char] = 0

        self.dictionary[char] += 1
        '''


