#Power of any number

base = int(input("Enter Base : "))
exp = int(input("Enter Exponent : "))
sum = 1

for i in range(1,exp+1):
    sum =sum * base
print(sum)
