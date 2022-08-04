#Sum of 2 Prime Numbers

n = int(input("Enter Number : "))
flag = False
a = []

for i in range(2,n):
    for j in range(2,i):
        if(i%j==0):
            flag = True
            break
        else:
            flag = False
    if(not flag):
        a.append(i)
print(a)
sum = 0
flag = False

for i in a:
    for j in range(0,len(a)):
        sum = int(i) + int(a[j])
        if(sum == n):
            print(i,a[j])
            flag = True
if(not flag):
    print("Prime Addition Not Satisfied....")
