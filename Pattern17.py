# Pattern Floyd's Triangle

# n = int(input("Enter Number : "))
n = 5
a = 0
b = 1
for i in range(0,n):
    for j in range(i,-1,-1):
        if(j%2==0):
            print(b,end="")
            
        else:
            print(a,end="")
    print()
