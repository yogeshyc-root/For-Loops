# Octal to Decimal

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
print(sum)

