# 循环版本
def binary_search1(list, key):
    first = 0
    last = len(list) - 1
    while first < last:
        mid = int((first + last) / 2)
        if key < list[mid]:
            last = mid - 1
        elif key > list[mid]:
            first = mid + 1
        else:
            return mid
    return False

"""
python3:
/是精确除法，//是向下取整除法

3/2=1.5

python2:

1 "/"所做的除法是以一种两个数或者多个数出现一个浮点数结果就以浮点数的形式表示，即float除法:3/2=1 3/2.0=1.5
2 "//"向下取整

"""
# 递归版本
def binary_search2(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                return binarySearch(alist[:midpoint], item)
            else:
                return binarySearch(alist[midpoint + 1:], item)


list = [1, 5, 8, 123, 22, 54, 7, 99, 300, 222]
result = BinarySearch(list, 22)
print(result)