"""
给定一个double类型的浮点数base和int类型的整数exponent。
求base的exponent次方。
"""

"""
本题思路：
从最基础的功能开始想，然后考虑全面问题

需要注意的地方:
当指数为负数的时候
当底数为零切指数为负数的情况
在判断底数base是不是等于0的时候,不能直接写base==0, 
因为计算机内表示小数时有误差,只能判断他们的差的绝对值是不是在一个很小的范围内
"""

"""
powerWithPositiveE 思路：
当n为偶数, a^n = a^(n/2) * a^(n/2)
当n为奇数, a^n = a^((n-1)/2) * a^((n-1)/2)) * a
利用右移一位运算代替除以2
利用位与运算代替了求余运算法%来判断一个数是奇数还是偶数
优化代码速度
"""

class Solution:
    def Power(self, base, exponent):
        # write code here
        if base == 0 and exponent == 0:
            return 0
        if base == 0 and exponent < 0:
            return False
        res = self.powerWithPositiveE(base, abs(exponent))
        if exponent < 0:
            res = 1 / res
        return res

    def powerWithPositiveE(self, base, exponent):
        if exponent == 0:
            return 1
        if exponent == 1:
            return base
        res = self.powerWithPositiveE(base, exponent >> 1)  # 递归调用,此时res是exponent右移一位之后得到的结果
        res = res ** 2  # 这里把res平方的原因是上一句中递归调用的exponent右移一位之后带入powerWithPositiveE函数，相当于最后函数得到的res是右移之前的结果的平方根
        if exponent & 1 == 1:
            res = res * base  # 这里乘的base是对应着exponent在此时最右面的一位（1），之前res对应着exponent除了最后一位的前面所有位的结果
        return res