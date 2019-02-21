# -*- coding: utf-8 -*-
"""
@Time    : 2018/11/28 4:50 PM
@Author  : libing
@Email   : icearl@qq.com
@File    : time.py
@Software: PyCharm
"""

"""当前时间"""
import datetime
# 当前时间
now = datetime.datetime.now()
today = datetime.datetime.today()
# 今天凌晨
today_0 = datetime.datetime(now.year, now.month, now.day, 0, 0, 0)
print('now:', now)
print('today', today)



