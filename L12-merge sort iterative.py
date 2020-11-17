#121910313025
#To implement merge sort iterative
def mergeSort(arr):
    current_size=1
    while current_size<len(arr)-1:
        left=0
        while left<len(arr)-1:
            mid=min((left + current_size - 1),(len(arr)-1))
             
            right=((2 * current_size + left - 1, 
                    len(arr) - 1)[2 * current_size 
                        + left - 1 > len(arr)-1]) 
                              
            merge(arr, left, mid, right) 
            left = left + current_size*2
              
        current_size = 2 * current_size 
 
# Merge Function 
def merge(arr, l, m, r): 
    n1 = m - l + 1
    n2 = r - m 
    L = [0] * n1 
    R = [0] * n2 
    for i in range(0, n1): 
        L[i] = arr[l + i] 
    for i in range(0, n2): 
        R[i] = arr[m + i + 1] 
 
    i, j, k = 0, 0, l 
    while i < n1 and j < n2: 
        if L[i] > R[j]: 
            arr[k] = R[j] 
            j += 1
        else:
            arr[k] = L[i] 
            i += 1
        k += 1
 
    while i < n1: 
        arr[k] = L[i] 
        i += 1
        k += 1
 
    while j < n2: 
        arr[k] = R[j] 
        j += 1
        k += 1
arr=[]
n=int(input("enter range:"))
for i in range(n):
    ele=int(input())
    arr.append(ele)
mergeSort(arr)
print("Sorted array :")
for i in range(len(arr)):
    print(arr[i])
    
