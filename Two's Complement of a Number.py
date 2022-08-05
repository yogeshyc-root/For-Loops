# Two's Complement of a Number

n = input("Enter Input :")
a=[]

for i in range(len(n)):
    if(n[i]=='0'):
        a.append(1)
    else:
        a.append(0)
c = 1
b = []

for i in range(len(a)-1,-1,-1):
    if(c==1 and a[i]==1):
        b.append(0)
        c = 1
    elif(c==1 and a[i]==0):
        b.append(1)
        c = 0
    else:
        b.append(a[i])
for i in range(len(b)-1,-1,-1):
    print(b[i],end='')

