def insertionSort(list):
    length = len(list)
    for i in range(1, length):
        item = list[i]
        j = i - 1
        while j >= 0:
            if list[j] > item:
                list[j + 1] = list[j]
                j -= 1
            else:
                break
        list[j + 1] = item

list = [3, 2, 4, 1, 59, 23, 13, 1, 3]
print(list)
insertionSort(list)
print(list)