# 希尔排序
# O(n * log(n))
def shell_sort(list):
    length = len(list)
    gap = int(length / 2)
    while gap > 0:
        # 分成 gap 个小组
        for i in range(gap):
            gapInsertionSort(list, gap, i)
        gap = int(gap / 2)


def gap_insertion_sort(list, gap, i):
    for j in range(i + gap, len(list), gap):
        item = list[j]
        last_index = j - gap
        while last_index >= 0:
            if list[last_index] > item:
                list[last_index + gap] = list[last_index]
                last_index -= gap
            else:
                break
        list[last_index + gap] = item

list = [3, 2, 4, 1, 59, 23, 13, 1, 3]
print(list)
shellSort(list)
print(list)