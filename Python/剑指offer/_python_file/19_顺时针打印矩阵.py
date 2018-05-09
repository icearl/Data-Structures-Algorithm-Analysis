# -*- coding:utf-8 -*-
"""
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下矩阵：
[[ 1,  2,  3,  4],
 [ 5,  6,  7,  8],
 [ 9, 10, 11, 12],
 [13, 14, 15, 16]]
则依次打印出数字 1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
"""

"""
本题思路：
方法一：
1. 逐层打印
2. 考虑边界条件
3. 考虑某条边打不打印

方法二：
旋转打印每一条边
"""

class Solution:
    """
    书上的思路
    """

    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        if matrix is None:
            return None
        rows = len(matrix)
        columns = len(matrix[0])
        start = 0
        while rows > start * 2 and columns > start * 2:
            self.PrintMatrixInCircle(matrix, columns, rows, start)
            start += 1
        print('')

    def PrintMatrixInCircle(self, matrix, columns, rows, start):
        endX = columns - 1 - start
        endY = rows - 1 - start

        # 从左到右打印一行
        for i in range(start, endX + 1):
            number = matrix[start][i]
            print(number, ' ', end='')

        # 从上到下打印一行
        if start < endY:
            for i in range(start + 1, endY + 1):
                number = matrix[i][endX]
                print(number, ' ', end='')

        # 从右到左打印一行
        if start < endX and start < endY:
            for i in range(endX - 1, start - 1, -1):
                number = matrix[endY][i]
                print(number, ' ', end='')

        # 从下到上打印一行
        if start < endX and start < endY - 1:
            for i in range(endY - 1, start, -1):
                number = matrix[i][start]
                print(number, ' ', end='')


class Solution:
    """
    更简单的思路
    """
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        result = []
        while matrix:
            result.extend(matrix.pop(0))  # matrix弹出第一行
            # 或者用result=result+matrix.pop(0),不能用result.append(matrix.pop(0))，
            # 因为它是一个列表不是元素，如果用append的话就将这段列表作为一个元素挂在后面了
            if not matrix:  # 注意这里判断语句的位置
                break
            matrix = self.turn(matrix)
        return result

    def turn(self, matrix):  # 将剩余的matrix部分逆时针旋转90°
        new_matrix = []
        row = len(matrix)  # 剩余部分的行数
        col = len(matrix[0])  # 剩余部分的列数
        for j in range(col):  # 对于每一列
            eachcolumn = []
            for i in range(row):  # 对于每一行
                eachcolumn.append(matrix[i][j])  # 这里每个循环eachcolumn以行的形式存储输出当前矩阵最左边的列
            new_matrix.append(eachcolumn)  # 相当于将当前矩阵最左边的列以行的形式一行一行的添加到newmatrix矩阵下面，此时行的顺序与目标矩阵的顺序是相反的
        new_matrix.reverse()  # 将newmatrix矩阵的行顺序倒过来 #另一种思路，生成newmatrix矩阵的时候直接用从最右边的列开始一行一行添加
        return new_matrix


matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]
matrix2 = [[1], [2], [3], [4], [5]]
matrix3 = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
S = Solution()
S.printMatrix(matrix)
S.printMatrix(matrix2)
S.printMatrix(matrix3)
# print(S.PrintMatrix(matrix))
# print(S.PrintMatrix(matrix2))
# print(S.PrintMatrix(matrix3))
