#Octal to Hexadecimal

from types import new_class


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

b = []
for i in range(0,new):
    rem = new%16
    new//=16
    if(rem>9):
        if(rem==10):
            b.append('A')
        elif(rem==11):
            b.append('B')
        elif(rem==12):
            b.append('C')
        elif(rem==13):
            b.append('D')
        elif(rem==14):
            b.append('E')
        elif(rem==15):
            b.append('F')
        else:
            pass
    else:
        b.append(rem)
    if(n==0):
        break
b.append(new)

for i in range(len(b)-1,-1,-1):
    print(b[i],end="")
