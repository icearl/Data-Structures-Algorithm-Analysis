"""
把 s 分两半，左边的应该是W，右边的应该是E，如果不是，那就计算不是的个数和
如：
'EEW' -> 1
'WWW' -> 0
问，怎么切，这个和最小。
"""
def min_sum2(s):
    length = len(s)
    cnt_w = 0
    for char in s:
        if char == 'W':
            cnt_w += 1
    # print('cnt_w', cnt_w)
    min_res = res = cnt_w
    for char in s:
        if char == 'E':
            res += 1
        if char == 'W':
            res -= 1
        if res < min_res:
            min_res = res
    return min_res

a = min_sum('WWEEW')
print(a)