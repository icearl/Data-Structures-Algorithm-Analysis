'''
书：25
输入一颗二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
'''


"""
递归
空：空
只有一个节点：
    基本情况 - 相等：返回[[root]]
    递归 - 不相等，继续：
        除了根节点，后面的路径递归搜索, left 和 right, 
        合并根节点加上后面的：
            left + right 形式 : [[1, 3], [1,1,1]]
            对 left + right 的每个元素前面加上 root.val
"""

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 不好用
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径/
    def FindPath(self, root, sum):
        if root is None:
            return []
        # 只有一个元素
        if root.left is None and root.right is None:
            if sum == root.val:
                return [[root.val]]
            else:
                return []
        stack = []
        leftStack = self.pathSum(root.left, sum - root.val)
        for i in leftStack:
            i.insert(0, root.val)
            stack.append(i)
        rightStack = self.pathSum(root.right, sum - root.val)
        for i in rightStack:
            i.insert(0, root.val)
            stack.append(i)
        return stack

    # 优化写法
    def pathSum(self, root, sum):
        if not root:
            return []
        if root.left == None and root.right == None:
            if sum == root.val:
                return [[root.val]]
            else:
                return []
        a = self.pathSum(root.left, sum - root.val) + self.pathSum(root.right, sum - root.val)
        return [[root.val] + i for i in a]

# 用这个
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if root is None or expectNumber is None:
            return []
        # 结束条件：如果成立的话此时是最下面的叶节点并且之前的点的和等于expectNumber
        if root is not None and root.left is None and root.right is None and root.val == expectNumber:
            return [[root.val]]
        # 存结果
        res = []
        # 注意这里之后的递归函数的输入的和为减去这次节点的val
        left = self.FindPath(root.left, expectNumber-root.val)
        right = self.FindPath(root.right, expectNumber-root.val)
        for i in left + right:
            res.append([root.val]+i)
        return res

pNode1 = TreeNode(10)
pNode2 = TreeNode(5)
pNode3 = TreeNode(12)
pNode4 = TreeNode(4)
pNode5 = TreeNode(7)

pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5

S = Solution()
print(S.FindPath(pNode1, 22))
# 测试用例：[1,-2,-3,1,3,-2,null,-1]  -1
# 测试用例：[-2, None, -3] -5
