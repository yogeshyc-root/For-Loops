#Compare two numbers using If condition

n1 = int(input("Enter Number 1 : "))
n2 = int(input("Enter Number 2 : "))

if(n1==n2):
    print("Numbers are Equal...")
else:
    print(n1,"is not equal to",n2)

if(n1>n2):
    print(n1,"is Greater than",n2)

if(n1>=n2):
    print(n1,"Greater than or equal to",n2)

if(n1<n2):
    print(n1,"is less than",n2)
