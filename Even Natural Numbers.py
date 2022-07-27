#EVEN Natural Numbers

n = int(input("Enter The limit: "))
n1 = int(input("Enter How many numbers to be sum"))
sum = 0
for i in range(1,n+1):
    if(i%2==0):
        print(i,end=" ")
        sum = sum+i
        n1-=1
        if(n1==0):
            break
print("Sum is",sum)
