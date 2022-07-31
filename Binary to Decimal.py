#Binary to Decimal

n = input("Enter Number : ")
sum = 0
j = 0

for i in n:
    sum = int(n[int(i)]) * (2**int(j)) + sum
    j+=1
print(sum)
