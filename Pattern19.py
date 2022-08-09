# Pattern Pyramid of Digits

# n = int(input("Enter Number : "))
n = 5
a = 1
for i in range(0,n):
    for j in range(i,n):
        print(" ",end="")
        a = i+1
    for j in range(i+1):
        print(a,end="")
        a+=1
        b = a-2
    for j in range(j,0,-1):
        print(b,end="")
        b-=1
    print()
    
