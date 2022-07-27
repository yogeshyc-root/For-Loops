#Sum of the series (9 + 99 + 999 + .......)

n = int(input("Enter the Numbre : "))
sum = 0

for i in range(1,n+1):
    sum = sum + ((10**i)-1)
print(sum)
