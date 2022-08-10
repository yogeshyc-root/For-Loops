# Pattern Pyramid like Alphabet
a = []
for i in range(65,91):
    a.append(chr(i))

# n = int(input("Enter Number of Letters : "))
n = 5
k = 0
for i in range(0,n):
    for j in range(i,n):
        print(" ",end = " ")
        k = 0
    for j in range(i):
        print(a[k],end=" ")
        k +=1
    for j in range(i+1):
        print(a[k],end = " ")
        k-=1
    print()