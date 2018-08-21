# -*- coding: utf-8 -*-

""" 书：59
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


# # O(n * k) 不可取
# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        length = len(num)

        if size > length or size == 0:
            return []
        tmax = []
        for i in range(length - size + 1):
            tmax.append(max(num[i:i + size]))

        return tmax


"""
注意：
如果是求滑动窗口的和，那对每个窗口不用全遍历。
只要减去前面的一个，加上后面的一个，就可以了。
# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        length = len(num)
        if size > length:
            return None
        win_sum = 0
        for i in range(size):
            win_sum += num[i]
        for j in range(1, length - size + 1):
            if (j + size) > size:
                return win_sum
            win_sum -= num[j - 1]
            win_sum += num[j + size - 1]
        return win_sum
"""

"""
本题正确思路：
核心：对每个窗口，维护最大值队列（）【就像是求滑动窗口的和一样】
1、初始化
2、更新的时候考虑：
    1、 怎么去掉前面的一个
    2、 怎么加上后面的一个
"""

# O(n) 解法，用这个
class Solution:
    def maxInWindows(self, num, size):
        if num == [] or num is None or size <= 0:
            return []
        # 保存结果的list
        deque = []
        if len(num) >= size:
            # 队列，保存，里面存的是值递减的 index
            index = []
            # 初始化 index
            for i in range(size):
                while len(index) > 0 and num[i] > num[index[-1]]:
                    index.pop()
                index.append(i)
            # 添加结果
            deque.append(num[index[0]])
            for i in range(size, len(num)):
                # 更新右边
                while len(index) > 0 and num[i] >= num[index[-1]]:
                    index.pop()
                # 去掉第一个
                if len(index) > 0 and size <= i - index[0]:
                    index.pop(0)
                index.append(i)
                # 添加本次结果
                deque.append(num[index[0]])
        return deque