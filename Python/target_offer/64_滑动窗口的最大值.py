# -*- coding: utf-8 -*-
"""
@Time    : 2018/8/15 下午5:14
@Author  : libing
@Email   : icearl@qq.com
@File    : 64_滑动窗口的最大值.py
@Software: PyCharm
"""

"""
题：
给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。
例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么一共存在6个滑动窗口，
他们的最大值分别为{4,4,6,6,6,5}；

针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个： 
{[2,3,4],2,6,2,5,1}， 
{2,[3,4,2],6,2,5,1}， 
{2,3,[4,2,6],2,5,1}， 
{2,3,4,[2,6,2],5,1}， 
{2,3,4,2,[6,2,5],1}， 
{2,3,4,2,6,[2,5,1]}。
"""


# O(n1)最大值
# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        # write code here

        length = len(num)

        if size > length or size == 0:
            return []
        tmax = []
        for i in range(length - size + 1):
            tmax.append(max(num[i:i + size]))

        return tmax
