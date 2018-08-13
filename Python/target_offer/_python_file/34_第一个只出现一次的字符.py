'''
在一个字符串(1<=字符串长度<=10000，全部由大写字母组成)中找到第一个只出现一次的字符。
'''

"""
构造哈希表：char: time_of_showup
"""
# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        if s is None or s == '':
            return -1

        alphabet = {}
        for char in s:
            if char not in alphabet.keys():
                alphabet[char] = 0
            alphabet[char] += 1
        for char in s:
            if alphabet[char] == 1:
                return s.index(char)
        return -1

s = Solution()
print(s.FirstNotRepeatingChar('abaccdeff'))