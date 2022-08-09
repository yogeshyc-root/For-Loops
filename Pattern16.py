# Pattern Matrix

n = int(input("Enter Number : "))
a = 0
b = 0
for i in range(0,n):
    for j in range(0,n):
        print(a,end="")
        a+=1
    print()
    a=b+1