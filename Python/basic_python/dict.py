# 键 key / 值 value 对，key 不重复


# 定义, key是不可变的就好
a = {}
b = {
    'a': 1,         # 字符串
    1: 2,           # 数字
    (1, 2): 2,      # tuple
}


# 添加 / 更新
a['b'] = 3
a.update(
    {
        'a': 1,     # 字符串
        1: 2,       # 数字
        (1, 2): 2,  # tuple
    }
)
a.update(b)


# 以列表返回一个字典所有的键
a.keys()


# 以列表返回字典中的所有值
a.values()

# 以列表返回可遍历的(键, 值) 元组数组
# python3 没有 iteritems，只有 items
a.items()
for k, v in a.items():
    print(k, v)