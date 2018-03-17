# 二叉树
class Tree(object):
    def __init__(self, element=None):
        self.element = element
        self.left = None
        self.right = None

    def pre_order_traversal_1(self, root):
        """
        前序遍历, 递归法
        """
        # 这个是前序遍历
        if root is None:
            return None
        print(self.element)
        self.left.pre_order_traversa_l()
        self.right.pre_order_traversa_l()

    def pre_order_traversal_2(self, root):
        """
        前序遍历，非递归实现
        :param root:
        :return:
        """
        if root is None:
            return
        my_stack = []
        node = root
        while node or my_stack:
            while node:
                # 从根节点开始，一直找它的左子树
                print(node.val)
                my_stack.append(node)
                node = node.lchild
            # while结束表示当前节点node为空，即前一个节点没有左子树了
            node = my_stack.pop()
            # 开始查看它的右子树
            node = node.rchild

    def in_order_traversal_1(self, root):
        if root is None:
            return None
        self.in_order_traversal_1(root.lchild)
        print(root.val)
        self.in_order_traversal_1(root.rchild)

    def in_order_traversal_2(self, root):
        if root == None:
            return
        myStack = []
        node = root
        while node or myStack:
            while node:
                # 从根节点开始，一直找它的左子树
                myStack.append(node)
                node = node.lchild
            # while结束表示当前节点node为空，即前一个节点没有左子树了
            node = myStack.pop()
            print(node.val)
            # 开始查看它的右子树
            node = node.rchild

    def postOrder1(self, root):
        """
        后序遍历，递归
        :param root:
        :return:
        """
        if root == None:
            return
        self.postOrder(root.lchild)
        self.postOrder(root.rchild)
        print
        root.val

    def postOrder2(self, root):
        """
        后序遍历
        :param root:
        :return:
        """
        if root == None:
            return
        myStack1 = []
        myStack2 = []
        node = root
        myStack1.append(node)
        while myStack1:
            # 这个while循环的功能是找出后序遍历的逆序，存在myStack2里面
            node = myStack1.pop()
            if node.lchild:
                myStack1.append(node.lchild)
            if node.rchild:
                myStack1.append(node.rchild)
            myStack2.append(node)
        while myStack2:
            # 将myStack2中的元素出栈，即为后序遍历次序
            print
            myStack2.pop().val

    def levelOrder(self, root):
        """
        层序遍历
        :param root:
        :return:
        """
        if root == None:
            return
        myQueue = []
        node = root
        myQueue.append(node)
        while myQueue:
            node = myQueue.pop(0)
            print
            node.val
            if node.lchild != None:
                myQueue.append(node.lchild)
            if node.rchild != None:
                myQueue.append(node.rchild)

    def reverse(self):
        '''
        交换左右节点的左右子树
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