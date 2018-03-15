class Tree(object):
    def __init__(self, element=None):
        self.element = element
        self.left = None
        self.right = None

    def traversal(self):
        """
        树的遍历, 是一个递归操作
        """
        # 这个是前序遍历
        print(self.element)
        if self.left is not None:
            self.left.traversal()
        if self.right is not None:
            self.right.traversal()

    def reverse(self):
        '''
        交换左右子树
        :return:
        '''
        self.left, self.right = self.right, self.left
        if self.left is not None:
            self.left.reverse()
        if self.right is not None:
            self.right.reverse()


def test():
    # 手动构建二叉树
    # 为什么手动这么麻烦呢, 因为一般都是自动生成的
    # 这里只需要掌握性质就好
    t = Tree(0)
    left = Tree(1)
    right = Tree(2)
    t.left = left
    t.right = right
    # 遍历
    t.traversal()


if __name__ == '__main__':
    test()

'''
二叉树的价值：
用于搜索 → 二叉搜索树
'''