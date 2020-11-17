#121910313025
#To implement selection sort  iterative
arr=[]
n=int(input("enter range:"))
for i in range(n):
    ele=int(input())
    arr.append(ele)
#code begins
for i in range(len(arr)):
    min_indx=i
    for j in range(i+1,len(arr)):
        if arr[min_indx]>arr[j]:
            min_indx=j
#swap
    arr[i],arr[min_indx]=arr[min_indx],arr[i]
#print
print("Sorted array is :")
for i in range(len(arr)):
    print(arr[i])
