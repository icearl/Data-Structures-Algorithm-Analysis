'''
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
'''

# 核心：定义一个新的比较函数，然后调用排序函数。
# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            return ""
        # Python 2.x 返回列表。
        # Python 3.x 返回迭代器。
        num=map(str,numbers)#map操作，将numbers里的元素都变成字符串
        # sort文档:http://python-reference.readthedocs.io/en/latest/docs/list/sort.html
        # cmp说明:http://www.runoob.com/python/func-number-cmp.html
        num.sort(lambda x,y:cmp(x+y,y+x))
        return ''.join(num)#字符串利用Join添加元素