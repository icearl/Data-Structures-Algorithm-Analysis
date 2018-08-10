'''
书：24
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。
假设输入的数组的任意两个数字都互不相同。
二叉搜索树对于每一个非叶子节点, 均有结点左子节点<当前节点<结点右子节点
'''

"""
思路：先假定序列是后续搜索的顺序，再根据条件判断

二叉搜索树 - 概念：
    若任意节点的左子树不空，则左子树上所有节点的值均小于它的根节点的值；
    若任意节点的右子树不空，则右子树上所有节点的值均大于它的根节点的值；
    任意节点的左、右子树也分别为二叉搜索树；
    没有键值相等的节点。
后序遍历：左子树-右子树-根节点
"""

# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST1(self, sequence):
        if sequence == [] or sequence is None:
            return False

        root = sequence[-1]
        length = len(sequence)
        index = 0
        # 二叉搜索树的左子树结点小于根节点
        while sequence[index] < root: #left最终为root的左子树的节点个数，求出左子树节点个数就知道了左子树和右子树各自节点个数
            index += 1

        # 二叉搜索树的右子树结点大于根结点
        # 这个循环中范围起始点必须是index+1, 不能为index
        # 因为当root结点前的所有元素小于root的时候,index=length-2,
        # 此时sequence[index]<root, 但是按照range(index, length-1),
        # 第一个元素sequence[j]==sequence[index] < root, 返回False, 实际应该返回True才对
        # 而使用index+1, 因为已经默认index>root, 所以从后面一个开始盘算右子树结点是否大于root, 也不会影响结果
        for j in range(index+1, length-1):
            if sequence[j] < root:
                return False

        left = True
        if index > 0:
            left = self.VerifySquenceOfBST(sequence[:index])

        right = True
        if index < length-1:
            right = self.VerifySquenceOfBST(sequence[index:length-1])
        return left and right

    def VerifySquenceOfBST2self, sequence):
        # write code here
        length = len(sequence)
        if length == 0:
            return False
        if length == 1:
            return True
        root = sequence[-1]
        left = 0
        while sequence[left] < root: #left最终为root的左子树的节点个数，求出左子树节点个数就知道了左子树和右子树各自节点个数
            left += 1
        for j in range(left, length-1):#对右子树中的节点进行判断
            if sequence[j] < root:
                return False
        #递归调用，对左子树右子树内部进行判断
        return self.VerifySquenceOfBST(sequence[:left]) or self.VerifySquenceOfBST(sequence[left:length-1])

array = [5, 7, 6, 9, 11, 10, 8]
array2 = [7, 4, 6, 5]
array3 = [1, 2, 3, 4, 5]
S = Solution()
print(S.VerifySquenceOfBST(array))
print(S.VerifySquenceOfBST(array2))
print(S.VerifySquenceOfBST(array3))