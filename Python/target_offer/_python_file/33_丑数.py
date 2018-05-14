'''
把只包含因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含因子7。
习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
'''

"""
用时间换空间：
丑数的构成就是一个丑数 * 2/3/5
维护一个有序丑数，每次增加一个最小的丑数
怎么增加：维护三个下标，指的是刚刚超过当前最大丑数的2/3/5下标
"""

# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        if index is None and len(index) <= 0:
            return 0

        uglyNumbers = [1]*index
        nextIndex = 1

        index2 = 0
        index3 = 0
        index5 = 0

        while nextIndex < index:
            minVal = min(uglyNumbers[index2]*2, uglyNumbers[index3]*3, uglyNumbers[index5]*5)
            uglyNumbers[nextIndex] = minVal

            while uglyNumbers[index2]*2 <= uglyNumbers[nextIndex]:
                index2 += 1
            while uglyNumbers[index3]*3 <= uglyNumbers[nextIndex]:
                index3 += 1
            while uglyNumbers[index5]*5 <= uglyNumbers[nextIndex]:
                index5 += 1

            nextIndex += 1

        return uglyNumbers[-1]