'''
书：61
随机从扑克牌中抽出了5张牌,判断是不是顺子,
决定大\小 王(0)可以看成任何数字,并且A看作1,J为11,Q为12,K为13。
'''

"""
看 joker 的数量能不能填充所需任意值的数量
"""


class Solution:
    def IsContinuous(self, numbers):
        if not numbers:
            return False
        numbers.sort()
        zeroNum = numbers.count(0)
        for i, v in enumerate(numbers[:-1]):
            if v != 0:
                if numbers[i + 1] == v:
                    return False
                zero_need = (numbers[i + 1] - v) - 1
                zeroNum = zeroNum - zero_need
                if zeroNum < 0:
                    return False
        return True


test = ['A', 3, 2, 5, 0]
test2 = [0, 3, 1, 6, 4]
s = Solution()
print(s.IsContinuous(test2))










