'''
将一个字符串转换成一个整数，要求不能使用字符串转换整数的库函数
'''

class Solution:
    def StrToInt(self, s):
        """
        检查非法输入情况
        :param s:
        :return:
        """
        # write code here
        # 先排除异常特殊情况
        if s in ['','-','+','+-','-+']:
            return 0
        count = 0 #用来统计字符串中不符合规定的字符
        # 只要有非法字符就不过
        for i in s:
            # 检查字母
            if i not in '0123456789+-':
                count += 1
        # 只要-+号不在第一位就不过
        for i in s[1:]:
            if i not in '0123456789':
                count += 1
        if count:
            return 0
        return int(s)

# -*- coding:utf-8 -*-
class Solution:
    # 如果输出是0, 通过检查flag判断输入不合法还是输入直接是'0'
    def StrToInt(self, s):
        """
        不能用 int 内置函数时，怎么做
        :param s:
        :return:
        """
        flag = False
        if s == None or len(s) < 1:
            return 0
        numStack = []
        dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        for i in s:
            if i in dict.keys():
                numStack.append(dict[i])
            elif i == '+':
                continue
            elif i == '-':
                continue
            else:
                return 0
        print(numStack)
        ans = 0
        if len(numStack) == 1 and numStack[0] == 0:
            flag = True
            return 0
        for i in numStack:
            ans = ans*10 + i
        if s[0] == '-':
            ans = 0 - ans
        return ans
