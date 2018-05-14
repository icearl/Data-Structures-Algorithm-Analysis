'''
书：22题
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。
假设压入栈的所有数字均不相等。
例如序列1,2,3,4,5是某栈的压入顺序，序列4，5,3,2,1是该压栈序列对应的一个弹出序列，
但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）
'''


"""
栈的特点是‘先进后出’，比如说12345，有可能1刚进栈就出栈了，其它数全进去了才出，就会产生15432，以此类推就可以；
相反43512就不行，因为当4首先出栈，则说明1，2，3三个元素已经入栈，则出栈序列中1不可能在2之前。
就是说比前面弹出的数小的数在后面弹出的顺序一定是递减的，因为它们是在前面交大之后的数弹出的，
说明他们压进去之后没有弹出，所以弹出的顺序是倒序。

意思是可能第一个序列的数是分批压入的，并且有的数可能压进去就直接弹出了，
比如体重给出的弹出顺序是45321就是先压进去123，然后压4，弹出4，压5，弹出剩下的5321

解决这个问题很直观的想法就是建立一个辅助栈，把输入的第一个序列中的数字依次压入该辅助栈，
并根据第二个序列的顺序及弹出规则依次从该辅助栈中弹出数字。

辅助栈的弹出规则是：
判断一个序列是不是栈的弹出序列的规律：最开始辅助栈为空，从第一个序列的头开始向辅助栈中压数字，
    如果下一个第二个序列弹出的数字刚好是辅助栈栈顶数字，那么从辅助栈直接弹出，记录弹出顺序。
    如果第二个序列下一个弹出的数字不在栈顶，我们把压栈序列中还没有入栈的数字压入辅助栈，
直到把下一个需要弹出的数字压入栈顶为止。如果所有的数字都压入栈了仍然没有找到下一个弹出的数字，
那么该序列不可能是一个弹出序列。
"""
# -*- coding:utf-8 -*-
class Solution:
    # 方法1
    def IsPopOrder(self, pushV, popV):
        if pushV == [] or popV == []:
            return False

        stack = []
        for i in pushV:
            stack.append(i)
            if stack[-1] != popV[0]:
                continue
            else:
                stack.pop()
                popV.pop(0)
        while len(stack) > 0 and stack[-1] == popV[0]:
            stack.pop()
            popV.pop(0)

        if len(stack) == 0:
            return True
        else:
            return False

    # 方法2, 进行了优化, 用这个
    def IsPopOrder2(self, pushV, popV):
        if pushV == [] or popV == []:
            return False
        stack = []
        for i in pushV:
            stack.append(i)
            while len(stack) != 0 and stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)
        if len(stack):
            return False
        else:
            return True

pushV = [1, 2, 3, 4, 5]
popV = [4, 5, 3, 2, 1]
popVF = [4, 5, 2, 1, 3]
S = Solution()
print(S.IsPopOrder2(pushV, popVF))