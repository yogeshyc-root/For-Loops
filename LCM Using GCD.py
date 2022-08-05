# LCM of 2 Numbers using HCF

def gcde(a,b):
    if(a>b):
        min = b
    else:
        min = a

    for i in range(min,0,-1):
        if(a%i==0 and b%i==0):
            gcd = i
            return gcd

n1 = int(input("Enter Number 1 : "))
n2 = int(input("Enter Number 2 : "))
gcd = 0
gcd = gcde(n1,n2)

lcm = 0
lcm = (n1*n2)/gcd
print(lcm)
