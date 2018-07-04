"""132. Palindrome Partitioning II
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

返回符合要求的最少分割次数。

示例:

输入: "aab"
输出: 1
解释: 进行一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。
"""

"""
动态规划https://blog.csdn.net/zhaohengchuan/article/details/75097093
"""

class Solution:
    def minCut(self, s):
        """
        https://blog.csdn.net/zhaohengchuan/article/details/75097093
        # dp solution
        # isPal[i][j] means if substring i..j is palindrome
        # cut[i] means minimum cut needed for sub string s[0:i+1]
        # At each i, default cut is i, reduce it by checking all j..i for j = 0:i+1 to see if
        # any j..i is palindrome
        :type s: str
        :rtype: int
        """


        if not s: return 0
        n = len(s)
        cut = [0] * n
        isPal = [[False] * n for _ in range(n)]

        # Single char is palindrome
        for i in range(n):
            for j in range(n):
                if i == j:
                    isPal[i][j] = True

        for i in range(n):
            # At most the number of cuts will be i because we can cut up it to all single chars
            cut[i] = i
            # Iterate all j up to and include i
            for j in range(i + 1):
                # if the substring from j..i is a palindome, we can reduce it's cut
                if s[i] == s[j] and (i - j < 2 or isPal[j + 1][i - 1]):
                    isPal[j][i] = True
                    # if we are able to have j == 0, then s[0:i+1] is a palindrome so cut[i] = 0`
                    if j == 0:
                        cut[i] = 0
                    # otherwise we need to add 1 cut for previous segment and the current palindrome
                    else:
                        cut[i] = min(cut[i], cut[j - 1] + 1)
        return cut[n - 1]