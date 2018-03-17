def selectionSort(list):
    length = len(list)
    # 依次从左到右，找到最小的放在左边
    for i in range(length):
        min_index = i
        for j in range(i + 1, length):
            if list[j] < list[min_index]:
                min_index = j
        list[i], list[min_index] = list[min_index], list[i]
    return list

list=[3, 2, 4, 1, 59, 23, 13, 1, 3]
print(list)
selectionSort(list)
print(list)

