def shellSort(list):
    length = len(list)
    gap = int(length / 2)
    while gap > 0:
        for i in range(gap):
            gapInsertionSort(list, gap, i)
        gap = int(gap / 2)

def gapInsertionSort(list, gap, i):
    for j in range(i + gap, len(list), gap):
        item = list[j]
        k = j - gap
        while k >= 0:
            if list[k] > item:
                list[k + gap] = list[k]
                k -= gap
            else:
                break
        list[k + gap] = item

list = [3, 2, 4, 1, 59, 23, 13, 1, 3]
print(list)
shellSort(list)
print(list)