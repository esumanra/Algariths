def insertion_sort(lis):
    for j in range(1, len(lis)):
        i = j - 1
        key = lis[j]

        while i >= 0 and lis[i] > key:
            lis[i + 1] = lis[i]
            i -= 1
        lis[i + 1] = key
    return lis


lis = [9, 6, 2, 7]

insertion_sort(lis)

print(lis)
