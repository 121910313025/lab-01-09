#121910313025
#To implement insertion sort using recursive
def insertionSortRecursive(arr,n):
    # base case
    if n<=1:
        return
     
    # Sort first n-1 elements
    insertionSortRecursive(arr,n-1)

       
    last = arr[n-1]
    j = n-2
      
    while (j>=0 and arr[j]>last):
        arr[j+1] = arr[j]
        j = j-1
 
    arr[j+1]=last
     
# A utility function to print an array of size n
def printArray(arr,n):
    for i in range(n):
        print(arr[i])
arr=[]
m=int(input("Enter range:"))
for i in range(m):
    ele=int(input())
    arr.append(ele)
n = len(arr)
insertionSortRecursive(arr, n)
printArray(arr, n)
 
