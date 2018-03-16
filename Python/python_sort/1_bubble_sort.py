# -*- codBing:utf-8 -*-
# 冒泡排序,O(n2)

# 一般冒泡
def bubble_sort1(list):
    length = len(list)
    for index in range(length):
        for i in range(1, length - index):
            if list[i-1] > list[i]:
                list[i], list[i-1] = list[i-1], list[i]
    return list

# 优化后的冒泡,识别是否已经排序，如果已经排序，就停止遍历
def bubble_sort2(list):
    length = len(list)
    exchanged = True
    for index in range(length):
        if exchanged == False:
            break
        exchanged =False
        for i in range(1, length - index):
            if list[i-1] > list[i]:
                list[i], list[i-1] = list[i-1], list[i]
                exchanged = True
    return list


#一下为测试其正确性：
list = [10,23,1,53,654,54,16,646,65,3155,546,31]
print(bubble_sort1(list))
