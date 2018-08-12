'''
书：42
输入一个整型数组,数组里有整数也有负数。
数组中一二或连续的多个整数组成一个子数组。求所有子数组的和的最大值。
要求时间复杂度为O(n)
'''

"""
动态规划分析
1、 子状态：以某一个字符为尾子串的最大和
2、 基本情况:第一个启动 
3、 递推式

cur_sum <= 0 那就加上当前 arr[i]，否则置cur_sum为arr[i]

aList[i-1] + array[i] 与 array[i]比较，哪个大取哪个
"""
# -*- coding:utf-8 -*-
class Solution:
    # 动态规划 空间O(1)
    def FindGreatestSumOfSubArray(self, array):
        if array == None or len(array) <= 0:
            return 0

        cur_sum = 0
        max_sum = array[0]
        for i in range(len(array)):
            if cur_sum <= 0:
                cur_sum = array[i]
            else:
                cur_sum += array[i]

            if cur_sum > max_sum:
                max_sum = cur_sum

        return max_sum
    # 动态规划 空间O(n)
    def FindGreatestSumOfSubArray2(self, array):
        if array == None or len(array) <= 0:
            return 0
        aList = [0]*len(array)
        for i in range(len(array)):
            if i == 0 or aList[i-1] <= 0:
                aList[i] = array[i]
            else:
                aList[i] = aList[i-1] + array[i]
        return max(aList)



alist = [1, -2, 3, 10, -4, 7, 2, -5]
s = Solution()
print(s.FindGreatestSumOfSubArray2(alist))