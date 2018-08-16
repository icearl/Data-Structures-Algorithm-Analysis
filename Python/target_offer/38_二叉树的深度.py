'''书：55
输入一棵二叉树，求该树的深度。
从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
'''

"""
递归思路
"""

class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if pRoot is None:
            return 0

        depth_left = self.TreeDepth(pRoot.left)
        depth_right = self.TreeDepth(pRoot.right)

        return 1 + max(depth_left, depth_right)