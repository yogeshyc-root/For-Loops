#Find the index of the element in an array = [10,2,5,7,23]

arr = [10,2,5,7,23]
print(arr)
n = int(input("Enter the element : "))

for i in range(0,len(arr)):
    if(arr[i] == n):
        print(i)
        break
