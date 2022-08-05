# Sum of Digits of an Integer

n = int(input("Enter Number : "))
sum = 0
rem = 0


for i in range(0,n):
    rem = n%10
    sum = sum + rem
    n//=10
    if(n==0):
        break
print(sum)
