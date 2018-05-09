"""
长度为 n 的 list，每个元素为 pi（代表逾期的概率），问 k 个逾期的概率。
"""

"""
用动态规划的方法
p(n, k) = p(n - 1, k - 1) * pn + p(n - 1, k) * (1 - pn)
"""


def gailv(arr, k):
    length = len(arr)
    res = [1] * length
    p0 = arr[0]
    res[0] = 1 - p0
    res[1] = p0
    for i in range(1, length):
        index = i + 1
        min_index = min(k, index)
        for j in range(min_index, 1, -1):
            p_cur = arr[i]
            res[j] = res[j - 1] * p_cur + res[]