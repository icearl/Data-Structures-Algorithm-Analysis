'''书：57
找出所有和为S的连续正数序列
输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序
'''

"""
思路：
维护两端两个数
"""
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        if tsum < 3:
            return []
        small = 1
        big = 2
        # 加1后二进制的形式右移一位，相当于除2之后向上取整，
        # 因为在python2中只有除法中包括浮点数的时候，结果才会有小数，因此此时不能用math.ceil()（向上取整函数）
        middle = int((tsum + 1) / 2)
        curSum = small + big
        output = []
        # 因为大于 mid 的两个数的和就会比 tsum 大了
        while small < middle:
            if curSum == tsum:
                output.append(range(small, big + 1))
                big += 1
                curSum += big
            elif curSum > tsum:
                curSum -= small
                small += 1
            else:
                big += 1
                curSum += big
        return output

s = Solution()
print(s.FindContinuousSequence2(15))