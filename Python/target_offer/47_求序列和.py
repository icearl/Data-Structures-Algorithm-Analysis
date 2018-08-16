# -*- coding: utf-8 -*-
"""
@Time    : 2018/8/15 上午9:58
@Author  : libing
@Email   : icearl@qq.com
@File    : 47_求序列和.py
@Software: PyCharm
"""

"""
求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
"""

# -*- coding:utf-8 -*-
class Solution:
    def Sum_Solution(self, n):
        # write code here
        def f(x,y):
            return x+y
        return reduce(f,range(n+1))