# Series sum of series 1 - X^2/2! + X^4/4!-.... upto nth term

x = int(input("Enter X Value : "))
n = int(input("Enter Limit : "))

sum = 1
a = 2

for i in range(2,n+1):
    fact = 1
    for j in range(2,a+1):
        fact  = fact * j
    if(i%2==0):
        sum = sum - ((x**a)/fact)
        a+=2
    else:
        sum = sum + ((x**a)/fact)
        a+=2
print(sum)