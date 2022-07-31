#Pattern 

n = int(input("Enter the Number : "))
num = 1
for i in range(0,n):
    for j in range(i,n):
        print(end=" ")
    for j in range(i+1):
        print(num,end = " ")
        num+=1
    print()
