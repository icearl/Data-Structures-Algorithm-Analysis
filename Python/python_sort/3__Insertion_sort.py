# 插入排序：
# 始终在列表的较低位置维护一个排序的子列表。然后将每个新项 “插入” 回先前的子列表。
#O(n^2 )


def insertionSort(list):
    length = len(list)
    for i in range(1, length):
        item = list[i]
        last_index = i - 1
        while last_index >= 0:
            # 如果前面有比 item 大的，就把 item 往前插
            if list[last_index] > item:
                list[last_index + 1] = list[last_index]
                last_index -= 1
            else:
                break
        list[last_index + 1] = item


li = [3, 2, 4, 1, 59, 23, 13, 1, 3]
print(li)
insertionSort(li)
print(li)