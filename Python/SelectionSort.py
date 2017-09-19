def selectionSort(list):
    length = len(list)
    for i in range(length):
        minIndex = i
        for j in range(i + 1, length):
            if list[j] < list[minIndex]:
                min = j
        list[i], list[min] = list[min], list[i]
    return list

def swap(list, i, j):
    list[i], list[j] = list[j], list[i]

list=[3, 2, 4, 1, 59, 23, 13, 1, 3]
print(list)
selectionSort(list)
print(list)

