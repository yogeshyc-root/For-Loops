#Sum of n terms of Natural Numbers and respective numbers

n = int(input("Enter the Number : "))
sum = 0
for i in range(1,n+1):
    print(i,end=" ")
    sum = sum + i
print("\nSum is : ",sum)
