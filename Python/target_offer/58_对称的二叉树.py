# -*- coding: utf-8 -*-
"""
@Time    : 2018/8/15 下午5:09
@Author  : libing
@Email   : icearl@qq.com
@File    : 58_对称的二叉树.py
@Software: PyCharm
"""

"""
题：
请实现一个函数，用来判断一颗二叉树是不是对称的。
注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
"""


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetrical1(self, pRoot1, pRoot2):
        if pRoot1 == None and pRoot2 == None:
            return True
        if pRoot1 == None or pRoot2 == None:  # 两者都为真的情况在上一条过滤掉了
            return False
        if pRoot1.val != pRoot2.val:
            return False

        return self.isSymmetrical1(pRoot1.left, pRoot2.right) and self.isSymmetrical1(pRoot1.right, pRoot2.left)
        # 左子树的左支与右子树的右支比较 左子树的右支和右子树的左支比较

    def isSymmetrical(self, pRoot):
        # write code here
        return self.isSymmetrical1(pRoot, pRoot)
