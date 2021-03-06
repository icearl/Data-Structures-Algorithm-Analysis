'''
书：58
输入一个英文句子, 翻转句子中单词的顺序,但单词内字符的顺序不变
为简单起见, 标点符号和普通字母一样处理
'''

"""
思路：
先对各个单词内部局部翻转，再对整体翻转
"""


# 方法一：最简单
class Solution:
    # 直接利用Python的语句进行字符串的翻转
    def ReverseSentence2(self, s):
        l = s.split(' ')
        return ' '.join(l[::-1])
# 方法二：方法一的解释版
class Solution:
    def ReverseSentence(self, s):
        # write code here
        if not s:
            return s
        # 单词保持先后，单词之间的先后顺序反转
        s = s.split(" ")
        news = []
        for word in range(len(s)-1, -1, -1):
            news.append(s[word])
            # if word:
            #     news.append(" ")
        return " ".join(news)

# 方法三：书上的版本
class Solution:
    def reverse(self, s):
        s = list(s)
        i = 0
        length = len(s)
        while i < (length + 1) >> 1:
            s[i], s[length - 1 - i] = s[length - 1 - i], s[i]
        return ''.join(s)

    def ReverseSentence(self, s):
        if not s:
            return None
        if len(s) == 1:
            return s
        s.split()
        res = []
        for i in s:
            i = self.reverse(i)
            res.append(i)
        return ''.join(res[:])




str = 'I am a student.'
s = Solution()
print(s.ReverseSentence2(str))