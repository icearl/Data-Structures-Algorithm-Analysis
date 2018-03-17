# 计数排序
# O(n)
def countingSort(alist, k):
    length = len(alist)
    sortedList = [0 for i in range(length)]
    countingList = [0 for i in range(k + 1)]
    # 每个数字有几个
    for item in alist:
        countingList[item] += 1
    # 每个数字上的数量加上之前的叠加
    for i in range(1, len(countingList)):
        countingList[i] += countingList[i - 1]
    for item in alist:
        index = countingList[item] - 1
        countingList[item] -= 1
        sortedList[index] = item
    return sortedList

list=[3, 2, 4, 1, 59, 23, 13, 1, 3]
print(list)
list = countingSort(list, 59)
print(list)