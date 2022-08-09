# Series sum of series 1 - X^2/2! + X^4/4!-.... upto nth term

x = int(input("Enter X Value : "))
n = int(input("Enter Limit : "))

sum = 1
fact = 1

for i in range(0,n):
    for j in range(1,i):
        fact = fact*j
        print(fact)
    if(i%2==0):
        sum = sum + ((x**i)/fact)
        print("+------------->",sum)
    else:
        sum = sum - ((x**i)/fact)
        print("'-'------------->",sum)
print(sum)