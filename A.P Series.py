#Sum of A.P Series

n1 = int(input("Enter Strat Value : "))
n2 = int(input("Enter Limit : "))
n3 = int(input("Enter Difference : "))

sum = n1
sum1 = n1

for i in range(n1,n2):
    sum = sum + n3
    #print(sum)
    sum1 = sum + sum1
print(sum1)
