#Pattern 

n = int(input("Enter the Number : "))

for i in range(0,n):
    for j in range(i,n):
        print(" ",end="")
    for j in range(i+1,0,-1):
        print(j,end = "")
    print()