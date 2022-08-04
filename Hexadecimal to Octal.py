# Hexadecimal to Octal

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
b=[]
rem = 0

for i in range(0,new):
    rem = new%8
    new//=8
    b.append(rem)
    if(new==0):
        break
for i in range(len(b)-1,-1,-1):
    print(b[i],end="")