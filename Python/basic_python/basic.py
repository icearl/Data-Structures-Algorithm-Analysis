# -*- coding:utf-8 -*-
"""
从python2.2开始，便有两种除法运算符："/"、"//"。两者最大区别在：
python2.2前的版本和python2.2以后3.0以前的版本的默认情况下，"/"所做的除法是以一种两个数或者多个数出现一个浮点数结果就以浮点数的形式表示，即float除法

"//"所做的除法则不相同，"//"不管两者出现任何数，都以整除结果为准，不对小数部分进行处理，直接抛弃，也就是整除法
链接：http://www.jianshu.com/p/9034aafb50aa
"""
# 三元运算
a = 1 if 2 < 1 else 2

# 格式化输出
# 1. % (不好，最好别用)
year = 10
fuck = '艹'
print('我%d岁了，%s'% (year, fuck))
# 2. .format(用它就完事了)
year = 10
fuck = '艹'
print('我{}岁了，{}'.format(year, fuck))

