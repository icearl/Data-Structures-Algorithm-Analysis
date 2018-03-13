def countingSort(list, k):
    length = len(list)
    sortedList = [0 for i in range(length)]
    countingList =  [0 for i in range(k + 1)]
    for item in list:
        countingList[item] += 1
    for i in range(1, len(countingList)):
        countingList[i] += countingList[i - 1]
    for item in list:
        index = countingList[item] - 1
        sortedList[index] = item
        countingList[item] -= 1
    return sortedList

list=[3, 2, 4, 1, 59, 23, 13, 1, 3]
print(list)
list = countingSort(list, 59)
print(list)