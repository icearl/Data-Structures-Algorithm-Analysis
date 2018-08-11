'''
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
要求不能创建任何新的结点，只能调整树中结点指针的指向。
'''

"""
根据二叉搜索树生成一个列表，然后在列表中定义左右指针
二叉搜索树：
若任意节点的左子树不空，则左子树上所有节点的值均小于它的根节点的值；
若任意节点的右子树不空，则右子树上所有节点的值均大于它的根节点的值；
任意节点的左、右子树也分别为二叉查找树；
没有键值相等的节点。
"""

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        def Convert(self, pRootOfTree):
            if pRootOfTree is None:
                return None
            if pRootOfTree.left is None and pRootOfTree.right is None:
                return pRootOfTree
            # 处理左子树
            left = self.Convert(pRootOfTree.left)
            if left is not None:
                p_left = left
                # 找左子树最大结点
                while p_left.right is not None:
                    p_left = p_left.right
                # 连接根与左子树最大结点
                p_left.right, pRootOfTree.left = pRootOfTree, p_left

            # 处理右子树
            right = self.Convert(pRootOfTree.right)
            if right is not None:
                # 连接根与右子树最小结点
                pRootOfTree.right, right.left, = right, pRootOfTree

            if left is not None:
                return left
            else:
                return pRootOfTree

pNode1 = TreeNode(8)
pNode2 = TreeNode(6)
pNode3 = TreeNode(10)
pNode4 = TreeNode(5)
pNode5 = TreeNode(7)
pNode6 = TreeNode(9)
pNode7 = TreeNode(11)
'''
        8
    6       10
5      7 9      11
'''
pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5
pNode3.left = pNode6
pNode3.right = pNode7

S = Solution()
newList = S.Convert(pNode1)
print(newList.val)