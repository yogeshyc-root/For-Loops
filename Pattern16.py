# Pattern Matrix

# n = int(input("Enter Number : "))
n = 5
a = 0
b = -1
for i in range(0,n):
    a=b+1
    for j in range(0,n):
        print(a,end="")
        a+=1
        if(a==i):
            a=0
        if(a==n):
            a=0

    print()
    b+=1