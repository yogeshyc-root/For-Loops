# Pattern odd number of rows reverse

# n = int(input("Enter Number : "))
n = 7
a = 1
b = 0
for i in range(1,n+1):
    a = 1
    for j in range(i+1):
        print(" ",end="")
    for j in range(i,n):
        print(a,end="")
        a+=1
        b = a
    for j in range(i,n+1):
        print(b,end="")
        if(j!=n):
            b-=1
    print()
