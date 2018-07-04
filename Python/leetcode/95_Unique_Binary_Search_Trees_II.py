"""
给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。

示例:

输入: 3
输出:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
解释:
以上的输出对应以下 5 种不同结构的二叉搜索树：

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""

"""
拆分，递归：
还是对每个 n ，找到一个数作为根结点，剩余的数分别划入左子树或者右子（树递归得到）。  
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self.dfs(1, n)

    def dfs(self, start, end):
        if start > end:
            return None
        result = []
        for root_val in range(start, end + 1):
            left_tree = self.dfs(start, root_val - 1)
            right_tree = self.dfs(root_val + 1, end)
            for l in left_tree or [None]:
                for r in right_tree or [None]:
                    node = TreeNode(root_val)
                    node.left, node.right = l, r
                    result.append(node)
        return result
