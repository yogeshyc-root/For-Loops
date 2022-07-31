#Pattern 

#n = int(input("Enter the Number : "))
n = 5
for i in range(0,n):
    for j in range(i,n):
        print(" ",end="")
    for j in range(i):
        print("*",end ="")
    for j in range(i+1):
        print("*",end="")
    print()
