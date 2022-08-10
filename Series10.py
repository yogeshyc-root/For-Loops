# Sum of Series x - x^3 + x^5 + ......

x = int(input("Enter X Value : "))
n = int(input("Enter Limit : "))

sum = x
a = 3

for i in range(2,n+1):
    if(i%2==0):
        sum = sum - (x**a)
        a+=2
    else:
        sum = sum + (x**a)
        a+=2
print(sum)