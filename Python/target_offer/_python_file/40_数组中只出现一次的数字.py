# -*- coding: utf-8 -*-
"""
@Time    : 2018/8/13 下午11:00
@Author  : libing
@Email   : icearl@qq.com
@File    : 40_数组中只出现一次的数字.py
@Software: PyCharm
"""

"""书：56
一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
"""

# 方法一：
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        tmp = []
        for a in array:
            if a in tmp:
                tmp.remove(a)
            else:
                tmp.append(a)
        return tmp

# 方法二：哈希
    def FindNumsAppearOnce(self, array):
        if array == [] or array is None:
            return []
        dic = {}
        res = []
        for num in array:
            if num not in dic.keys():
                dic[num] = 0
            dic[num] += 1
        for num in array:
            if dic[num] == 1:
                res.append(num)
        return res
# 方法三：书上异或，没看

