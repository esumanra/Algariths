# Python implementation of heapsort


def minHeapify(arr, heap_size, i):
    """
    Min Heapify's from given index

    Parameters:
    arr (list): array
    heap_size (int): heapsize of the heap
    i (int): start index of heapify process
    """
    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < heap_size and arr[i] > arr[l]:
        smallest = l
    if r < heap_size and arr[smallest] > arr[r]:
        smallest = r

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        minHeapify(arr, heap_size, smallest)


def heapSort(arr):
    size = len(arr)

    for i in range(size, -1, -1):
        minHeapify(arr, size, i)

    for i in range(size-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        minHeapify(arr, i, 0)


if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    heapSort(arr)
    n = len(arr)
    print("Sorted array is")
    for i in range(n):
        print("%d" % arr[i]),
