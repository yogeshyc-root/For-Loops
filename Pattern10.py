#Pattern 

n = int(input("Enter the Number : "))

for i in range(1,n+1):
    for j in range(i,n+1):
        print(i,end="")
        i+=1
    for j in range(i+1):
        print(" ",end="")
    print()
