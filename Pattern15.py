#Power of 2 Pattern

n = int(input("Enter Number : "))

a = 0

for i in range(0,n):
    a = 0
    for j in range(i,n):
        print(" ",end = " ")
    for j in range(1,i+1):
        print(2**a,end = " ")
        a = j
    for j in range(i+1):
        print(2**a,end=" ")
        a-=1
    print()