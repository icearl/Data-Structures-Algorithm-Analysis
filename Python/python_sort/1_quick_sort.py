# 快速排序
# 一种交换排序法
from random import randint
# 快排总函数
def sort(alist):
    quickSort(alist, 0, len(alist) - 1)

# 指定从哪开始快排
def quickSort(arr, i, j):
    if i < j:
        base_index = randomizedPartition(arr, i, j)
        quickSort(arr, i, base_index - 1)
        quickSort(arr, base_index + 1, j)

# 随机取值分割
def randomizedPartition(arr, i, j):
    rand_index = randint(i, j)
    arr[i], arr[rand_index] = arr[rand_index], arr[i]
    return partition(arr, i, j)

# 快排排序过程
def partition(arr, i, j):
    base = arr[i]
    while i < j:
        while i < j and arr[j] >= base:
            j -= 1
        if i < j:
            arr[i] = arr[j]
            i += 1
        while (i < j) and (arr[i] <= base):
            i += 1
        if i < j:
            arr[j] = arr[i]
    arr[i] = base
    return i



list=[3, 2, 4, 1, 59, 23, 13, 1, 3]
print(list)
sort(list)
print(list)