#Binary to Hexadecimal

n = input("Enter Number : ")
n1 = len(n)-1
sum = 0
j = 0

for i in range(n1,-1,-1):
    sum = int(n[int(i)]) * (2**int(j)) + sum
    j+=1
new = sum
print(new)
rem = 0
a = []
for i in range(0,len(str(new))):
    rem = new%16
    new//=16
    print(new)
    a.append(rem)
b = []
for i in range(len(a)-1,-1,-1):
    if(a[i]>9):
        if(a[i]==10):
            b.append('A')
        elif(a[i]==11):
            b.append('B')
        elif(a[i]==12):
            b.append('C')
        elif(a[i]==13):
            b.append('D')
        elif(a[i]==14):
            b.append('E')
        elif(a[i]==15):
            b.append('F')
        else:
            pass
    else:
        b.append(a[i])
for i in b:
    print(i,end="")

