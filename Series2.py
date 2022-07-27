#Sum of Series  (1*1) + (2*2) + ....... + (n*n)

n = int(input("Enter Number"))
sum = 0

for i in range(1,n+1):
    sum = sum + (i*i)
    
print(sum)
