# 无序表、顺序查找

def sequence_search(list, key):
    length = len(list)
    for i in range(length):
        if list[i] == key:
            return i
    return False

list = [1, 5, 8, 123, 22, 54, 7, 99, 300, 222]
result = sequence_search(list, 22)
print(result)

