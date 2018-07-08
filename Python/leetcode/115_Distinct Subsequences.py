# -*- coding: utf-8 -*-
"""
@Time    : 2018/7/8 下午5:38
@Author  : libing
@Email   : icearl@qq.com
@File    : 115_Distinct Subsequences.py
@Software: PyCharm
"""

""" 题目：不同的子序列
给定一个字符串 S 和一个字符串 T，计算在 S 的子序列中 T 出现的个数。

一个字符串的一个子序列是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。（例如，"ACE" 是 "ABCDE" 的一个子序列，而 "AEC" 不是）

示例 1:

输入: S = "rabbbit", T = "rabbit"
输出: 3
解释:

如下图所示, 有 3 种可以从 S 中得到 "rabbit" 的方案。
(上箭头符号 ^ 表示选取的字母)

rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^
示例 2:

输入: S = "babgbag", T = "bag"
输出: 5
解释:

如下图所示, 有 5 种可以从 S 中得到 "bag" 的方案。 
(上箭头符号 ^ 表示选取的字母)

babgbag
^^ ^
babgbag
^^    ^
babgbag
^    ^^
babgbag
  ^  ^^
babgbag
    ^^^
"""


class Solution:
    """
    自己写的，用的是递归，时间超时了，应该用下面的 dp 思路
    """
    def numDistinct(self, s, t):
        """
        :type s: str eg: "babgbag"
        :type t: str eg: "bag"
        :rtype: int
        """
        res_cnt = 0
        for i in range(len(s)):
            if s[i] == t[0]:
                if len(t) == 1:
                    res_cnt += 1
                else:
                    res_cnt += self.numDistinct(s[i + 1:], t[1:])
            else:
                continue
        return res_cnt

# 用这个
class Solution:
    def numDistinct(self, S, T):
        """
        思路：https://shenjie1993.gitbooks.io/leetcode-python/115%20Distinct%20Subsequences.html
        典型的动态规划问题，dp[i][j]表示字符串S[:i]和T[:j]的不同子序列数目，如果S[i-1]和T[j-1]不相等，
        那么只能在S[:i-1]和T[:j]中匹配，即dp[i][j] = dp[i-1][j]；而当S[i-1]和T[j-1]相等时，
        可以是这两个字符正好匹配，也可以忽略S[i-1]，使T[j-1]在S[:i-1]中匹配，
        所以dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]。
        :type s: str
        :type t: str
        :rtype: int
        """
        # dp 保存
        dp = [[0 for j in range(len(T) + 1)] for i in range(len(S) + 1)]
        # 最左边的那列初始化成 1
        for i in range(len(S) + 1):
            dp[i][0] = 1
        # 按上面的思路来
        for i in range(len(S)):
            for j in range(len(T)):
                if S[i] == T[j]:
                    dp[i + 1][j + 1] = dp[i][j+1] + dp[i][j]
                else:
                    dp[i+1][j+1] = dp[i][j + 1]
        return dp[len(S)][len(T)]

if __name__ == "__main__":
    S = "rabbbit"
    T = "rabbit"
    result = Solution().numDistinct(S, T)
    print(result)