#Prime number before entered input

n = int(input("Enter Number"))

flag = False
for i in range(n,1,-1):
    a = int(i**0.5)
    for j in range(2,a+1):
        if(i%j==0):
            flag = True
            break
        else:
            flag = False
    if(not flag):
        print(i,"Prime")
        break
