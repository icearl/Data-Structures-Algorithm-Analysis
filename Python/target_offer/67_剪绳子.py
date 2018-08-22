"""
给你一根长度为n的绳子，请把绳子剪成m段 (m和n都是整数，n>1并且m>1)
每段绳子的长度记为k[0],k[1],...,k[m].
请问k[0]*k[1]*...*k[m]可能的最大乘积是多少？

例如，当绳子的长度为8时，我们把它剪成长度分别为2,3,3的三段，此时得到的最大乘积是18.
"""

"""
本题思路：
先从简单的情况分析，找规律
动态规划
"""


def cut_rope(length):
    """
    剪绳子问题，采用动态规划
    """
    if length < 2:
        return 0  # 如果给的绳子小于2，没法剪，不符合题目要求，返回0
    if length == 2:
        return 1  # 如果长度是2，还必须至少剪一刀，只能是1*1 =1
    if length == 3:
        return 2  # 如果长度为3，只能是2*1 = 2 > 1*1*1 =1
    products = [None] * 50
    # products列表，放的是绳子长度最优的情况
    products[0] = 0
    products[1] = 1
    products[2] = 2
    products[3] = 3
    """
    当length > 3时，不要对3进行剪开，因为无论怎么剪，都小于3本身
    而大于3的绳子，剪开可能比本身大，或至少等于本身，3是一个底线
    为什么要定义products[1] = 1和products[2] = 2？
    因为：不可能绳子程度都是三的倍数，一定会需要1和2来保证相加起来等于绳子的长度。
    """
    for i in range(4, length + 1):  # 从长度为4的绳子开始
        # 求出从4到给出的绳子，每一个长度的最大乘积
        max = 0
        for j in range(1, i // 2 + 1):  # 从1到i//2+1师因为4*6和6*4一样，当到了中间相同的数字，乘积结束后就可以
            product = products[i] * products[i - j]
            if max < product:
                max = product
            product[i] = max
    max_product = products[length]
    return max_product
