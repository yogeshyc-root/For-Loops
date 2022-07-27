#Fibbonacci Series

n = int(input("Enter Number : "))
n1 = 0
n2 = 1

for i in range(0,n):
    print(n1,end=",")
    t = n1+n2
    n1 = n2
    n2 = t
    
