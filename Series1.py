#Sum of Series  1 + 1/2^2 + 1/3^3 + ....... + 1/n^n

n = int(input("Enter Number : "))
sum = 0
sum1 = 0
for i in range(1,n+1):
    sum = sum +1/(i**i)
print(sum)
