# Pattern odd number of rows

# n = int(input("Enter Number : "))
n = 5
a = 1
for i in range(0,n):
    a = 1
    for j in range(i,n):
        print(" ",end="")
    for j in range(i+1):
        print(a,end="")
        a+=1
    for j in range(j,0,-1):
        print(j,end="")
    print()
