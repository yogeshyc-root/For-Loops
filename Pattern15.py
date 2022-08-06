#Power of 2 Pattern

n = int(input("Enter Number : "))
temp = [1]
temp1=[]
print(n*' ',temp)
for j in range(0,n):
    for i in range(j,n+2):
        print(" ",end='')
    temp1.append(1)
    for i in range(1,len(temp)):
        temp1.append(2**i)
    temp1.append(1)
    print(temp1)
    temp = temp1
    temp1 = []
