# LCM of 2 Numbers

n1 = int(input("Enter Number 1 : "))
n2 = int(input("Enter Number 2 : "))
gcd = 0

if(n1>n2):
    min = n2
else:
    min = n1

for i in range(min,0,-1):
    if(n1%i==0 and n2%i==0):
        gcd = i
        break
print(gcd)
