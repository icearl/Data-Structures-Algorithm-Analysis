def BinarySearch(list, key):
    low = 0
    high = len(list) - 1
    while low < high:
        mid = int((low + high) / 2)
        if key < list[mid]:
            high = mid - 1
        elif key > list[mid]:
            low = mid + 1
        else:
            return mid
    return False

list = [1, 5, 8, 123, 22, 54, 7, 99, 300, 222]
result = BinarySearch(list, 22)
print(result)