'''
书：题38
输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
结果请按字母顺序输出。
输入描述:
输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。
'''

"""
从最简单的情况考虑
考虑递归和动态规划
分解，发现递归可以
分成两部分考虑
"""
# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # 考虑基础情况
        if not len(ss):
            return []
        if len(ss) == 1:
            return list(ss)
        # 字符串转成 list
        charList = list(ss)
        charList.sort()
        res_list = []
        for i in range(len(charList)):
            first_char = charList[i]
            # 有重复的话，就是一种
            if i > 0 and charList[i] == charList[i-1]:
                continue
            left_list = self.Permutation(''.join(charList[:i])+''.join(charList[i+1:]))
            for left in left_list:
                res_list.append(first_char + left)
        return res_list

    # 扩展习题, 生成字符的所有组合
    # 比如输入abc, 则他们的组合有['a', 'ab', 'abc', 'ac', 'b', 'bc', 'c'], ab和ba属于不同的排列, 但属于同一个组合
    def group(self, ss):
        if not len(ss):
            return []
        if len(ss) == 1:
            return list(ss)
        charList = list(ss)
        charList.sort()
        pStr = []
        for i in range(len(charList)):
            pStr.append(charList[i])
            if i > 0 and charList[i] == charList[i - 1]:
                continue
            # 核心区别
            temp = self.group(''.join(charList[i + 1:]))
            for j in temp:
                pStr.append(charList[i] + j)
            pStr = list(set(pStr))
            pStr.sort()
        return pStr

ss = 'acb'
S = Solution()
# print(S.Permutation(ss))
print(S.group(ss))