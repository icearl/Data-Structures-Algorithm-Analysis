"""
两个排序的数组A和B分别含有m和n个数，找到两个排序数组的中位数，要求时间复杂度应为O(log (m+n))。
"""

"""
思路：
https://blog.csdn.net/qq_14821023/article/details/50806849
https://www.jiuzhang.com/qa/1768/
"""

class Solution:
    """
    @param A: An integer array.
    @param B: An integer array.
    @return: a double whose format is *.5 or *.0
    """

    def findMedianSortedArrays(self, A, B):
        n = len(A) + len(B)
        if n % 2 == 1:
            return self.findKth(A, B, n / 2 + 1)
        else:
            smaller = self.findKth(A, B, n / 2)
            bigger = self.findKth(A, B, n / 2 + 1)
            return (smaller + bigger) / 2.0

    def findKth(self, A, B, k):
        if len(A) == 0:
            return B[k - 1]
        if len(B) == 0:
            return A[k - 1]
        if k == 1:
            return min(A[0], B[0])

        a = A[k / 2 - 1] if len(A) >= k / 2 else None
        b = B[k / 2 - 1] if len(B) >= k / 2 else None

        if b is None or (a is not None and a < b):
            return self.findKth(A[k / 2:], B, k - k / 2)
        return self.findKth(A, B[k / 2:], k - k / 2)