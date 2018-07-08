# -*- coding: utf-8 -*-
"""
@Time    : 2018/7/8 下午5:02
@Author  : libing
@Email   : icearl@qq.com
@File    : 120_triangle.py
@Software: PyCharm
"""

""" 题目：120. 三角形最小路径和
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。

例如，给定三角形：

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

说明：

如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。"""

"""思路
动态规划，从底到顶。维护一个 n（层数） 长的数组。
"""

class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        length = len(triangle)

        if triangle is None:
            return None

        dp_arr = triangle[-1]

        # 对行开始更新 dp_arr
        for line_index in range(length - 1):
            print('line_index', line_index)
            cur_li = triangle[- line_index - 2]
            lower_li = dp_arr

            for num_index in range(len(cur_li)):
                cur = cur_li[num_index]
                lower_left = lower_li[num_index]
                lower_right = lower_li[num_index + 1]

                if lower_left <= lower_right:
                    dp_arr[num_index] = lower_left + cur
                else:
                    dp_arr[num_index] = lower_right + cur
        return dp_arr[0]

if __name__ == "__main__":
    # print(Solution().minimumTotal([[-1], [2, 3], [1, -1, -3]]))
    print(Solution().minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
