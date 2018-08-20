# -*- coding: utf-8 -*-
"""
@Time    : 2018/8/15 下午5:13
@Author  : libing
@Email   : icearl@qq.com
@File    : 62_二叉搜索树的第 k 大节点.py
@Software: PyCharm
"""

"""
题：
给定一颗二叉搜索树，请找出其中的第k大的结点。
例如， 5 / \ 3 7 /\ /\ 2 4 6 8 中，按结点数值大小顺序第三个结点的值为4。
"""

"""
备注：
二叉查找树（英语：Binary Search Tree），也称二叉搜索树、有序二叉树（英语：ordered binary tree），排序二叉树（英语：sorted binary tree），是指一棵空树或者具有下列性质的二叉树：

若任意节点的左子树不空，则左子树上所有节点的值均小于它的根节点的值；

若任意节点的右子树不空，则右子树上所有节点的值均大于它的根节点的值；

任意节点的左、右子树也分别为二叉查找树；

没有键值相等的节点。

二叉搜索树节点的大小关系从小到大就是中序遍历

# 第三个节点是4
# 前序遍历5324768
# 中序遍历2345678
# 后序遍历2436875
# 所以是中序遍历，左根右
"""


# 不够规范,遍历 k 次就够了现在得 n 次
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        self.result = []
        self.midnode(pRoot)  # 根据中序遍历的顺序生成列表存储在result中
        if 0 < k <= len(self.result):
            return self.result[k - 1]
        else:
            return None

    def midnode(self, root):  # 中序遍历
        if root is None:
            return None
        self.midnode(root.left)
        self.result.append(root)
        self.midnode(root.right)