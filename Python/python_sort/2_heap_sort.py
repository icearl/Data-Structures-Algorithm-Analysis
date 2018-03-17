# 堆排序
# O(n * log(n))
# 一种选择排序
# 大顶堆：一种完全二叉树，每个节点的值 >= 其左右孩子节点的值

def MaxHeapify(heap,HeapSize,root):#在堆中做结构调整使得父节点的值大于子节点

    left = 2 * root + 1
    right = left + 1
    larger = root
    if left < HeapSize and heap[larger] < heap[left]:
        larger = left
    if right < HeapSize and heap[larger] < heap[right]:
        larger = right
    if larger != root:#如果做了堆调整则larger的值等于左节点或者右节点的，这个时候做对调值操作
        heap[larger],heap[root] = heap[root],heap[larger]
        MaxHeapify(heap, HeapSize, larger)


def BuildMaxHeap(heap):#构造一个堆，将堆中所有数据重新排序
    heap_size = len(heap)#将堆的长度当独拿出来方便
    for i in range(int(heap_size / 2 - 1), -1, -1):#从后往前出数
        MaxHeapify(heap, heap_size, i)


def HeapSort(heap):#将根节点取出与最后一位做对调，对前面len-1个节点继续进行对调整过程。
    BuildMaxHeap(heap)
    for i in range(len(heap)-1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        MaxHeapify(heap, i, 0)
    return heap


alist=[3, 2, 4, 1, 59, 23, 13, 1, 3]
print(alist)
HeapSort(alist)
print(alist)