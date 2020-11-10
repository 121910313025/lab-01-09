#To find the second smallest element in an array
#input array
arr=[]
n=int(input("Enter range: "))
print("Enter array elements: ")
for i in range(n):
    ele=int(input())
    arr.append(ele)

arr.sort()

print(arr[1])
