# -*- coding:utf-8 -*-
"""
题目：书 4
在一个二维数组(array 二维列表)中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
"""

# 一般思路：
# 特殊化，从特殊例子出发，思考普遍规律

# 本题思路：
# 从右上角开始找，如果比当前值小则列-1，比当前值大则行+1
# 图见 onenote

class Solution:
    # array 二维列表
    def find(self, target, array):
        # write code here
        row = len(array)
        col = len(array[0])

        i = 0
        j = col - 1

        while i < row and j >= 0:
            if array[i][j] == target:
                return True
            # 如果要找的在左边，那就 j - 1
            if array[i][j] > target:
                j -= 1
            if array[i][j] < target:
                i += 1

        return False

array = [[1, 2, 8, 9],
         [2, 4, 9, 12],
         [4, 7, 10, 13],
         [6, 8, 11, 15]]


findtarget = Solution()
print(findtarget.find(12, array))

