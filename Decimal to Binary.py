# Decimal to Binary

n = input("Enter Input : ")
a=[]
rem = 0

for i in range(0,int(n)):
    n = int(n)
    rem = n%2
    n//=2
    a.append(rem)
    if(n==0):
        break
for i in range(len(a)-1,-1,-1):
    print(a[i],end="")