#Pattern 

n = int(input("Enter the Number : "))

for i in range(0,n):
    num = 1
    for j in range(i+1):
        print(end=" ")
    for j in range(i,n):
        print(num,end = " ")
        num+=1
    print()
