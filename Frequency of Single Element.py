#Find a frequency of a single element

arr = [1,2,2,2,2,2,2,3,4,5,6,3,4,5,6,7,8,8,9,9]
print(arr)
n = int(input("Enter the Number : "))
count = 0

for i in range(0,len(arr)):
    if(arr[i]==n):
        count+=1
print(count)
