# Decimal to Hexadecimal

n = input("Enter Input : ")
a=[]
rem = 0

for i in range(0,int(n)):
    n = int(n)
    rem = n%16
    n//=16
    if(rem>9):
        if(rem==10):
            a.append('A')
        elif(rem==11):
            a.append('B')
        elif(rem==12):
            a.append('C')
        elif(rem==13):
            a.append('D')
        elif(rem==14):
            a.append('E')
        elif(rem==15):
            a.append('F')
        else:
            pass
    else:
        a.append(rem)
    if(n==0):
        break
for i in range(len(a)-1,-1,-1):
    print(a[i],end="")