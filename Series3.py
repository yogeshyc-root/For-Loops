#Sum of Series (1) + (1+2) + (1+2+3) + ..... + (1+2+3+......+n)

n = int(input("Enter Number ; "))

sum = 0

for i in range(1,n+1):
    for j in range(1,i+1):
        sum = sum +j
print(sum)
