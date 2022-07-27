#Sum of Digits

sum = 0
rem = 0
n = int(input("Enter Number"))

for i in range(0,n):
    rem = n%10
    sum = sum+rem
    n//=10
print(sum)
