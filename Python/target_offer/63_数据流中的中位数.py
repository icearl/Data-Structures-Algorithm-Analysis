# -*- coding:utf-8 -*-
"""
如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。
"""


class Solution:
    """
    数组实现:
    插入：正常插入，然后排序。O(n)
    取中位数：O(1)
    """
    def __init__(self):
        self.data = []

    def Insert(self, num):
        # 插入函数
        self.data.append(num)
        self.data.sort()

    def GetMedian(self, data):
        # 获取中位数的函数
        length = len(self.data)
        if length % 2 == 0:
            return (self.data[length // 2] + self.data[length // 2 - 1]) / 2.0  # /做除法是有一个数是浮点型就返回浮点型，//的结果始终抛弃小数返回整数
        else:
            return self.data[int(length // 2)]

class Solution:
    """
    堆实现
    """
    def __init__(self):
        self.left = []
        self.right = []
        self.count = 0
    def Insert(self, num):
        if self.count & 1 == 0:
            self.left.append(num)
        else:
            self.right.append(num)
        self.count += 1

    def GetMedian(self, x):
        if self.count == 1:
            return self.left[0]
        self.MaxHeap(self.left)
        self.MinHeap(self.right)
        if self.left[0] > self.right[0]:
            self.left[0], self.right[0] = self.right[0], self.left[0]
        self.MaxHeap(self.left)
        self.MinHeap(self.right)
        if self.count & 1 == 0:
            return (self.left[0] + self.right[0])/2.0
        else:
            return self.left[0]

    def MaxHeap(self, alist):
        length = len(alist)
        if alist == None or length <= 0:
            return
        if length == 1:
            return alist
        for i in range(length//2-1, -1, -1):
            k = i; temp = alist[k]; heap = False
            while not heap and 2*k < length-1:
                index = 2*k+1
                if index < length - 1:
                    if alist[index] < alist[index + 1]: index += 1
                if temp >= alist[index]: heap = True
                else:
                    alist[k] = alist[index]
                    k = index
            alist[k] = temp

    def MinHeap(self, alist):
        length = len(alist)
        if alist == None or length <= 0:
            return
        if length == 1:
            return alist
        for i in range(length//2-1, -1, -1):
            k = i; temp = alist[k]; heap = False
            while not heap and 2 * k < length - 1:
                index = 2 * k+1
                if index < length - 1:
                    if alist[index] > alist[index + 1]: index += 1
                if temp <= alist[index]:
                    heap = True
                else:
                    alist[k] = alist[index]
                    k = index
            alist[k] = temp