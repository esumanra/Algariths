import copy
# Using extra space O(N)

def remove_duplicates_using_extra_space(arr):
    output_arr = []
    j = 0
    for i in range(len(arr)-1):
        if arr[i] != arr[i+1]:
            output_arr.append(arr[i])
            j += 1

    output_arr.append(arr[-1])
    j += 1
    #print(output_arr)
    # for i in range(j):
    #     arr[i] = output_arr[i]
    arr[:] = list(output_arr)

    return j

def remove_duplicates_using_extra_space_2(arr):
    arr.append(float('inf'))
    output_arr = []
    j = 0
    for i in range(len(arr)-1):
        if arr[i] != arr[i+1]:
            output_arr.append(arr[i])
            j += 1

    arr[:] = list(output_arr)

    return j

# without extra space - inplace
def remove_duplicates(arr):
    arr.append(None)
    j = 0

    for i in range(len(arr)-1):
        if arr[i] != arr[i+1]:
            arr[j] = arr[i]
            j += 1
    return j

ar = [0,0,1,1,1,2,2,3,3,4,5]
end = remove_duplicates_using_extra_space(ar)
print("{}-{}".format('remove_duplicates_using_extra_space   ', ar[:end]))

ar = [0,0,1,1,1,2,2,3,3,4,5]
end = remove_duplicates_using_extra_space_2(ar)
print("{}-{}".format('remove_duplicates_using_extra_space_2 ', ar[:end]))

ar = [0,0,1,1,1,2,2,3,3,4,5]
end = remove_duplicates(ar)
print("{}-{}".format('remove_duplicates                     ', ar[:end]))
