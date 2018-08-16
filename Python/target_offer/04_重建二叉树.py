# -*- coding:utf-8 -*-
"""
重建二叉树：书 7
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和
       中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
"""

"""
一般思路：
1. 从简单例子考虑，画一个三个节点的二叉树来理解
2. 递归：
    1. 基本情况
    2. 递归式
        1. 调用本函数产生子结果
        2. 合并到当前规模

本题思路：
二叉树的遍历和序列的关系，以前序为主进行递归，利用中序的信息
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):#pre代表输入的前序遍历的顺序，tin代表输入的中序遍历的顺序
        # write code here
        if len(pre) == 0:
            return None
        if len(pre) == 1:
            return TreeNode(pre[0]) #返回一个TreeNode类的对象
        else:
            index_tin = tin.index(pre[0])
            cur_root = TreeNode(pre[0])
            cur_root.left = self.reConstructBinaryTree(pre[1:index_tin + 1], tin[: index_tin])#self.+函数名递归的方法
            #这一行中flag.left为根节点的左孩子，对其进行递归的二叉树打印
            #其中，pre[1:tin.index(pre[0])+1]中的1总体根节点的左孩子，即左子树的根节点，tin.index(pre[0])为总体根节点在中序排列中的位置
            #pre[1：tin.index(pre[0])+1]代表整个左子树中的节点, 后面的项+1是因为这个是先序遍历，前面是从总体的根节点开始的
            #tin[:tin.index(pre[0])]代表在中序遍历中整个左子树对应的序列
            #即整句话为对整个左子树递归调用reConstructBinaryTree函数，中间的pre和tin参数分别对应着左子树中所有节点对应的前序及中序排列的部分序列
            cur_root.right = self.reConstructBinaryTree(pre[index_tin + 1:], tin[index_tin + 1:])
            #如上，pre[tin.index(pre[0])+1:]中[tin.index(pre[0])+1:]代表右子树的根节点
            return cur_root

pre = [1, 2, 3, 5, 6, 4]
tin = [5, 3, 6, 2, 4, 1]
test = Solution()
newTree = test.reConstructBinaryTree(pre, tin)

# 按层序遍历输出树中某一层的值
def PrintNodeAtLevel(treeNode, level):
    if not treeNode or level < 0:
        return 0
    if level == 0:
        print(treeNode.val)
        return 1
    PrintNodeAtLevel(treeNode.left, level-1)
    PrintNodeAtLevel(treeNode.right, level-1)

# 已知树的深度按层遍历输出树的值
def PrintNodeByLevel(treeNode, depth):
    for level in range(depth):
        PrintNodeAtLevel(treeNode, level)

PrintNodeByLevel(newTree, 5)