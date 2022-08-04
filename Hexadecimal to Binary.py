# Hexadecimal to Binary

n = input("Enter Number : ")
a = 0
sum = 0
j = len(n)-1
for i in n:
    a = i
    if(a=='A'):
        sum = int(10 * (16**j)) + sum
    elif(a=='B'):
        sum = int(11 * (16**j)) + sum
    elif(a=='C'):
        sum = int(12 * (16**j)) + sum
    elif(a=='D'):
        sum = int(13 * (16**j)) + sum
    elif(a=='E'):
        sum = int(14 * (16**j)) + sum
    elif(a=='F'):
        sum = int(15 * (16**j)) + sum
    else:
        a = int(a)
        sum = int(a * (16**j)) + sum
    j-=1

new = sum

a=[]
rem = 0

for i in range(0,new):
    rem = new%2
    new//=2
    a.append(rem)
    if(new==0):
        break
for i in range(len(a)-1,-1,-1):
    print(a[i],end="")