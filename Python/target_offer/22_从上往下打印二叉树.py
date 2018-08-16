'''
书：32题
从上往下打印出二叉树的每个节点，同层节点从左至右打印。(打印到一行就行)
'''

'''
相当于按层遍历, 中间需要队列做转存
'''

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 1. 不分行从上到下打印二叉树
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom1(self, root):
        if not root:
            return []
        queue = [root]
        result = []
        while len(queue) > 0:
            currentRoot = queue.pop(0)
            result.append(currentRoot.val)
            if currentRoot.left is not None:
                queue.append(currentRoot.left)
            if currentRoot.right is not None:
                queue.append(currentRoot.right)
        return result

    # 2. 分行，从上到下打印二叉树
    def PrintFromTopToBottom2(self, root):
        # write code here
        if root is None:
            return []
        nodes = [root]
        res = []
        while nodes != []:
            # 不要用 cur_val = next_nodes = [] ,这样会让 cur_val 引向 next_nodes
            cur_val, next_nodes = [], []
            for i in nodes:
                cur_val.append(i.val)
                if i.left is not None:
                    next_nodes.append(i.left)
                if i.right is not None:
                    next_nodes.append(i.right)
            res.append(cur_val)
            nodes = next_nodes
        return res

    # 3. 分行，从上到下，之字型打印二叉树
    def PrintFromTopToBottom3(self, root):
        # write code here
        if root is None:
            return []
        nodes = [root]
        res = []
        left_to_right = True
        while nodes != []:
            # 不要用 cur_val = next_nodes = [] ,这样会让 cur_val 引向 next_nodes
            cur_val, next_nodes = [], []
            for i in nodes:
                cur_val.append(i.val)
                if i.left is not None:
                    next_nodes.append(i.left)
                if i.right is not None:
                    next_nodes.append(i.right)
            if not left_to_right:
                cur_val.reverse()
            res.append(cur_val)
            left_to_right = not left_to_right
            nodes = next_nodes
        return res

pNode1 = TreeNode(8)
pNode2 = TreeNode(6)
pNode3 = TreeNode(10)
pNode4 = TreeNode(5)
pNode5 = TreeNode(7)
pNode6 = TreeNode(9)
pNode7 = TreeNode(11)

pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5
pNode3.left = pNode6
pNode3.right = pNode7

S = Solution()
print(S.PrintFromTopToBottom3(pNode1))