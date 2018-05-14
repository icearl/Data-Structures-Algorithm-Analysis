"""
给定三个字符串 s1, s2, s3, 验证 s3 是否是由 s1 和 s2 交错组成的。

示例 1:

输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
输出: true
示例 2:

输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
输出: false
"""
class Solution:
    """
    @params s1, s2, s3: Three strings as description.
    @return: return True if s3 is formed by the interleaving of
             s1 and s2 or False if not.
    @hint: you can use [[True] * m for i in range (n)] to allocate a n*m matrix.
    """
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if s1 is None or s2 is None or s3 is None:
            return False
        if len(s1) + len(s2) != len(s3):
            return False
        # i + 1 * j + 1 维的存储 T/F 的矩阵
        interleave = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]
        # 初始化左上角
        interleave[0][0] = True
        # 初始化左边和上边的边
        for i in range(len(s1)):
            interleave[i + 1][0] = s1[:i + 1] == s3[:i + 1]
        for i in range(len(s2)):
            interleave[0][i + 1] = s2[:i + 1] == s3[:i + 1]
        # 状态转移方程
        for i in range(len(s1)):
            for j in range(len(s2)):
                # 先初始化为不行
                interleave[i + 1][j + 1] = False
                # 如果用 i ，那就看上一个走的 j 是不是可以
                if s1[i] == s3[i + j + 1]:
                    interleave[i + 1][j + 1] = interleave[i][j + 1]
                if s2[j] == s3[i + j + 1]:
                    interleave[i + 1][j + 1] |= interleave[i + 1][j]
        return interleave[len(s1)][len(s2)]

