#121910313025
#To implement insertion sort  iterative
def insertionSort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
#array inputs
arr=[]
n=int(input("enter range:"))
for i in range(n):
    ele=int(input())
    arr.append(ele)
insertionSort(arr)
print("The sorted array is:")
for i in range(len(arr)):
    print(arr[i])

