#Non-Prime numbers 1 to an upperbound

n = int(input("Enter Number : "))

flag = False

for i in range(3,n+1): #  is unique number and 2 is prime number
    for j in range(2,i):
        if(i%j==0):
            flag = True
            break
        else:
            flag = False
            break
    if(flag):
        print(i)
