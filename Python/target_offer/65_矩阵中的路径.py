"""书：12
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。
例如
a b c e
s f c s
a d e e
矩阵中包含一条字符串"bcced"的路径，
但是矩阵中不包含"abcb"路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
"""

"""
一般思路：回溯法
1. 遍历所有的可能起点，开始启动。
2. 对每个起点，递归。 

本题思路：
回溯法
注意，走过的格子不能再走，所以要做标记。
"""


# -*- coding:utf-8 -*-
# 方法一：好理解的思路
class Solution:
    def printMatrix(self, matrix, rows, cols, direction):
        if direction:
            print("---" + direction)
        for i in range(rows):
            for j in range(cols):
                print(matrix[cols * i + j], end=' ')

    def hasPath(self, matrix, rows, cols, path):
        # write code here
        for i in range(rows):
            for j in range(cols):
                # 任选一个格子作为路径的起点
                if matrix[i * cols + j] == path[0]:
                    if self.find(list(matrix), rows, cols, path[1:], i, j):
                        return True
        return False

    def find(self, matrix, rows, cols, path, i, j):
        if path == '':  # 后面没有了
            print('a')
            return True
        matrix[i * cols + j] = '0'  # 走过这个点之后将其设为"0"
        flag = flag1 = flag2 = flag3 = flag4 = False
        if j + 1 < cols and matrix[i * cols + j + 1] == path[0]:
            flag1 = self.find(matrix, rows, cols, path[1:], i, j + 1)
        if j - 1 >= 0 and matrix[i * cols + j - 1] == path[0]:
            flag2 = self.find(matrix, rows, cols, path[1:], i, j - 1)
        if i + 1 < rows and matrix[(i + 1) * cols + j] == path[0]:
            flag3 = self.find(matrix, rows, cols, path[1:], i + 1, j)
        if i - 1 >= 0 and matrix[(i - 1) * cols + j] == path[0]:
            flag4 = self.find(matrix, rows, cols, path[1:], i - 1, j)
        flag = flag1 or flag2 or flag3 or flag4
        return flag


# 方法二：书上的思路(用这个就完事了)
class Solution:
    # 主函数
    def hasPath(self, matrix, rows, cols, path):
        """

        :param matrix:二维数组
        :param rows: int
        :param cols: int
        :param path: str
        :return:
        """
        if matrix is None or rows < 1 or cols < 1 or path is None:
            return False
        # 一维数组，是否用过
        visited = [0] * (rows * cols)

        pathLength = 0
        # 遍历每个点，从每个点出发都要试
        for row in range(rows):
            for col in range(cols):
                if self.hasPathCore(matrix, rows, cols, row, col, path, pathLength, visited):
                    return True
        return False

    def hasPathCore(self, matrix, rows, cols, row, col, path, pathLength, visited):
        if len(path) == pathLength:
            return True

        hasPath = False
        if 0 <= row < rows and 0 <= col < cols and matrix[row * cols + col] == path[pathLength] and not \
                visited[row * cols + col]:

            pathLength += 1
            visited[row * cols + col] = True

            hasPath = self.hasPathCore(matrix, rows, cols, row, col - 1, path, pathLength, visited) or \
                      self.hasPathCore(matrix, rows, cols, row - 1, col, path, pathLength, visited) or \
                      self.hasPathCore(matrix, rows, cols, row, col + 1, path, pathLength, visited) or \
                      self.hasPathCore(matrix, rows, cols, row + 1, col, path, pathLength, visited)

            if not hasPath:
                pathLength -= 1
                visited[row * cols + col] = False

        return hasPath


# 测试
if __name__ == "__main__":
    # 调用测试
    _matrix = 'abcebfcsadee'
    # _path = 'see'
    _path = 'abad'
    path = Solution()
    path.printMatrix(_matrix, 3, 4, _path)
    print('\n')
    print(path.hasPath(list(_matrix), 3, 4, _path))

#
# abce
# bfcs
# adee
