# Octal to Binary 

n = int(input("Enter Number : "))

rem = 0
a = []
sum = 0

for i in range(0,n):
    rem = n%10
    n//=10
    a.append(rem)
    sum = (rem * (8**i)) + sum
    if(n==0):
        break

new = sum
rem = 0
b = []

for i in range(0,new):
    rem = new%2
    new//=2
    b.append(rem)
    if(new==0):
        break
for i in range(len(b)-1,-1,-1):
    print(b[i],end="")
