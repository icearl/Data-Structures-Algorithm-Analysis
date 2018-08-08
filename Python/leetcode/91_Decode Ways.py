# -*- coding: utf-8 -*-
"""
@Time    : 2018/7/8 下午7:23
@Author  : libing
@Email   : icearl@qq.com
@File    : 91_Decode Ways.py
@Software: PyCharm
"""

""" 91 解码方法 Decode Ways
一条包含字母 A-Z 的消息通过以下方式进行了编码：

'A' -> 1
'B' -> 2
...
'Z' -> 26
给定一个只包含数字的非空字符串，请计算解码方法的总数。

示例 1:

输入: "12"
输出: 2
解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
示例 2:

输入: "226"
输出: 3
解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
"""


class Solution:
    """递归方法，时间复杂度不行"""
    def is_2_vaild(self, s):
        int_2 = int(s)
        if 10 <= int_2 <= 26:
            return True
        else:
            return False

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or s == '':
            return 1
        if len(s) == 1 and s != '0':
            return 1
        if len(s) == 1 and s == '0':
            return 0

        if self.is_2_vaild(s[:2]):
            return self.numDecodings(s[2:]) + self.numDecodings(s[1:])
        else:
            if s[0] != '0':
                return self.numDecodings(s[1:])
            else:
                return 0


if __name__ == "__main__":
    print(Solution().numDecodings("01"))
    # print(Solution().numDecodings("110"))
    # assert Solution().numDecodings("110") == 1
    # assert Solution().numDecodings("40") == 0