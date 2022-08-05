#Checkboard Pattern

n = int(input("Enter Number : "))

b = "black"
w = "white"
t = "black"

for i in range(0,n):
    for j in range(0,n):
        print(t,end="-")
        t=w
        w=b
        b=t
    print()