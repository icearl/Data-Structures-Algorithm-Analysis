# -*- coding: utf-8 -*-
"""
@Time    : 2018/8/15 下午5:10
@Author  : libing
@Email   : icearl@qq.com
@File    : 61_序列化二叉树.py
@Software: PyCharm
"""

"""
题:
请实现两个函数，分别用来序列化和反序列化二叉树
"""

"""
解释：
序列化：根据给的树输出对应的字符串
反序列化：根据字符串构建出对应的树
"""

"""
思路：
分成三部分递归：
根节点、左子树、右子树
"""


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Serialize(self, root):
        # write code here
        # 如果是叶子节点的子节点（None节点），就返回一个特殊的字符，比如 '#'
        if root is None:
            return "#"
        return str(root.val) + "," + self.Serialize(root.left) + "," + self.Serialize(root.right)

    # 输入字符串，输出头节点
    def Deserialize(self, s):
        # write code here
        root, index = self.deserialize(s.split(","), 0)
        return root

    def deserialize(self, s, index):
        if s[index] == "#":  # 遇见空的树
            return None, index + 1  # 函数返回root和index两个值
        root = TreeNode(int(s[index]))  # 定义当前节点的.val
        index += 1
        root.left, index = self.deserialize(s, index)  # 定义当前节点的.left,里面的index不用+1（前面加过了）#s始终不变，index每次执行函数向后移一位
        root.right, index = self.deserialize(s, index)  # 定义当前节点的.right
        return root, index


