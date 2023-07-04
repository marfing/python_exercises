def find_smallest_difference(arr1, arr2):
    diff = -1
    for x in arr1:
        for y in arr2:
            temp = abs(x-y)
            if diff == -1 or temp < diff:
                    diff = temp
    return diff

def mergeSort(arr):
    size = len(arr)
    if size > 1:
        L = arr[:size//2]
        mergeSort(L)
        R = arr[size//2:]
        mergeSort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                  arr[k] = L[i]
                  i += 1
            else:
                 arr[k] = R[j]
                 j += 1
            k += 1
        while i < len(L):
             arr[k] = L[i]
             i+=1
             k+=1
        while j < len(R):
             arr[k] = R[j]
             j+=1
             k+=1

def find_small_diff_in_sorted(arr1, arr2):
    mergeSort(arr1)
    mergeSort(arr2)
    if len(arr1) < 1:
        arr1 = [0]
    if len(arr2) < 1:
         arr2 = [0]
    i = len(arr1)-1 
    j = len(arr2)-1
    diff = abs(arr1[i] - arr2[j])
    while i >= 0 and j >= 0:
        if arr1[i] == 0 and arr2[j] == 0:
             i -= 1
             j -= 1
             continue
        if diff == None:
             diff = abs(arr1[i] - arr2[j])
        temp = abs(arr1[i] - arr2[j])
        if temp < diff:
            diff = temp
        if arr1[i] > arr2[j]:
            if i > 0: i -= 1
            else: j -= 1
        else:
            if j > 0: j -= 1
            else: i -= 1
    return diff
        

if __name__ == '__main__':
    arr1 = [1,3,15,11,2]
    arr2 = [23,127,135,19,8]
    print(f'array1: {arr1}')
    print(f'array2: {arr2}')
    # mergeSort(arr1)
    # mergeSort(arr2)
    # print(f'Sorted arr1: {arr1}')
    # print(f'Sorted arr2: {arr2}')
    print(f'Smallest difference: {find_small_diff_in_sorted(arr1, arr2)}')
    
    #print(f'Smallest: {find_smallest_difference(arr1, arr2)}')