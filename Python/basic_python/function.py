# 函数参数:必选参数、默认参数、可变参数、关键字参数、命名关键字参数(顺序不能变)
# 1 必选参数: 必须填
def power(a, b)
    pass
# 2 默认参数：可填可不填
def power(x, n=2):
    pass
# 3 可变参数 *args
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
a = [1, 2, 3]
calc(4, 5)
calc(*a)
# 4 关键字参数

# 匿名函数-> 参数:返回值
lambda x: x * x
# 等价于
def f(x):
    return x * x

# map / reduce
# map(函数，iterable) 将传入的函数依次作用于序列的每个元素，并把结果作为新的 iterator 返回。
i = map(lambda x: x ^ 2, [1, 2, 3, 4, 5, 6, 7, 8, 9])    # 返回的是 Iterator,是惰性序列
li = list(i)    # 用 list() 把整个序列算出来，并返回一个 list
[i for i in map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])]    # 直接用列表生成器生成列表

# reduce
# 把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
from functools import reduce
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

# filter 也是把函数作用在后面序列的每个元素上，只是不全返回，而是根据函数的 True/False 来决定是否保留这个元素,返回的也是 iterator
def is_odd(n):
    return n % 2 == 1
list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
# 结果: [1, 5, 9, 15]