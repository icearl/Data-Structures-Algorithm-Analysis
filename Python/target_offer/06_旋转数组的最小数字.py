# -*- coding:utf-8 -*-
"""
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非递减排序(即后面的数大于等于前面的数)的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
"""

"""
一般思路：
排序数组中找一个数或统计某个数字出现的次数，都可以用二分法

本题思路：
方法一：遍历，蠢
方法二：二分法 - 思路 http://www.cnblogs.com/edisonchou/p/4746561.html
    维护两个指针，一个指向大数组，一个指向小数组，往中间缩小，知道两个指针碰上。
    注意两点：
    1. 把 0 个元素方法到后面怎么办
    2. 如果 sta，mid，end 相同怎么办  
"""

# 方法一：遍历
class Solution:
    def minNumberInRotateArray(self,rotateArray):
        if len(rotateArray)==0:
            return 0
        if len(rotateArray)==1:
            return rotateArray[0]
        mini = rotateArray[0]
        for i in range(0, len(rotateArray)):
            if rotateArray[i] < mini:
                mini = rotateArray[i]
        return mini


# 方法二: 二分法，没理解清楚
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray) == 0:
            return 0
        if len(rotateArray) == 1:
            return rotateArray[0]
        left = 0
        right = len(rotateArray) - 1
        while left <= right:
            if rotateArray[left] == rotateArray[right]:
                left += 1
                right -= 1
                # print left, " ", right

            else:
                mid = (left + right) / 2  # Python2中两个整形的除法只保留整数部分，如果left的右边贴着right的话mid更新之后等于left
                if left == mid:  # 当left挨着right，更新之后left==mid
                    break
                if rotateArray[mid] > rotateArray[right]:  # 此时最小值在mid和right中间,即右半边
                    left = mid
                elif rotateArray[mid] < rotateArray[left]:  # 此时最小值在mid和left中间，即左半边
                    right = mid
                else:
                    # print left, " ", right, "~~"
                    return rotateArray[left]
        return min(rotateArray[right], rotateArray[left])

# 方法三：二分法，用这个
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        length = len(rotateArray)

        if length == 0:
            return 0
        if length == 1:
            return rotateArray[0]

        sta, end = 0, length - 1
        # 意外情况1: 要时刻保证右边的值更大
        while rotateArray[sta] >= rotateArray[end]:
            # 两个指针挨上了，那么后面那个就是
            if end - sta == 1:
                return rotateArray[end]

            mid = (sta + end) / 2
            # 意外情况2，如果三者一样，要找中间的最小值
            if (rotateArray[sta] == rotateArray[mid]) and (rotateArray[mid] == rotateArray[end]):
                minimum = rotateArray[sta]
                for i in range(sta + 1, end + 1):
                    if minimum > rotateArray[i]:
                        minimum = rotateArray[i]
                return minimum

            if rotateArray[sta] <= rotateArray[mid]:
                sta = mid
            elif rotateArray[end] >= rotateArray[mid]:
                end = mid

        return rotateArray[mid]


