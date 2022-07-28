#Sum of Series : 1 + 11 + 111 + 1111 +.......n

n = int(input("Enter the Number : "))
sum = 1
sum1 = 0

for i in range(1,n+1):
    sum = sum + (10**i)
    #print(sum)
    sum1 = sum1 + sum
print(sum1)
