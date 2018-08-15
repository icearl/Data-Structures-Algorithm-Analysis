# -*- coding: utf-8 -*-
"""
@Time    : 2018/8/15 下午2:54
@Author  : libing
@Email   : icearl@qq.com
@File    : 51_构建乘积数组.py
@Software: PyCharm
"""

"""
题：
给定一个数组A[0,1,...,n-1],
请构建一个数组B[0,1,...,n-1],
其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。
不能使用除法。
"""

"""
思路：
链接：https://www.nowcoder.com/questionTerminal/94a4d381a68b47b7a8bed86f2975db46
来源：牛客网

解释下代码，设有数组大小为5。

对于第一个for循环
第一步：b[0] = 1;
第二步：b[1] = b[0] * a[0] = a[0]
第三步：b[2] = b[1] * a[1] = a[0] * a[1];
第四步：b[3] = b[2] * a[2] = a[0] * a[1] * a[2];
第五步：b[4] = b[3] * a[3] = a[0] * a[1] * a[2] * a[3];

然后对于第二个for循环
temp = 1
第一步
temp *= a[4] = a[4];  
b[3] = b[3] * temp = a[0] * a[1] * a[2] * a[4];

第二步
temp *= a[3] = a[4] * a[3];
b[2] = b[2] * temp = a[0] * a[1] * a[4] * a[3];

第三步
temp *= a[2] = a[4] * a[3] * a[2];  
b[1] = b[1] * temp = a[0] * a[4] * a[3] * a[2];

第四步
temp *= a[1] = a[4] * a[3] * a[2] * a[1];  
b[0] = b[0] * temp = a[4] * a[3] * a[2] * a[1];
由此可以看出从b[4]到b[0]均已经得到正确计算。
"""


# 跟书上思路一样
# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        if not A:
            return []

        # 计算前面一部分成绩
        num = len(A)
        B = [None] * num  # 先划定空间的目的是之后的循环会用到
        B[0] = 1
        for i in range(1, num):
            B[i] = B[i - 1] * A[i - 1]

        # 计算后面一部分乘积：
        # 从后向前
        # 保留上次的计算结果乘本轮新的数,因为只是后半部分进行累加，所以设置一个tmp,能够保留上次结果
        tmp = 1
        for i in range(num - 2, -1, -1):  # i最小取到0，此时循环为B[0]*A[1]*(A[2]*A[3]*A[4])
            tmp *= A[i + 1]
            B[i] *= tmp

        return B