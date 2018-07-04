"""
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

返回 s 所有可能的分割方案。

示例:

输入: "aab"
输出:
[
  ["aa","b"],
  ["a","a","b"]
]
"""

# 递归方法
class Solution:
    """
    将一个字符串分为前后两部分，
    如果第一部分是一个回文字符串，则对第二部分再次分割，不断递归，直到递归的终止条件——字符串为空为止；
    如果第一部分不是一个回文字符串，则尝试下一种分割方法。
    """
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        # 递归终止条件
        if s is None:
            return [[]]
        # 存储回文串结果
        result = []
        for i in range(len(s)):
            if self.is_palindrome(s[:i + 1]):
                # 得到后面的回文串的结果，拼上浅一部分
                for r in self.partition(s[i + 1:]):
                    result.append([s[:i + 1]] + r)
        return result

    def is_palindrome(self, s):
        for i in range(len(s) // 2):
            if s[i] != s[-(i + 1)]:
                return False
        return True