#Sum of G.P Series

n1 = int(input("Enter Strat Value : "))
n2 = int(input("Enter Limit : "))
n3 = int(input("Enter Ratio : "))

sum = n1

for i in range(1,n2):
    n1 *= n3
    sum = n1 + sum
print(sum)
