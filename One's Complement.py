#1's Complement of a Binary Number

n = input("Enter Input :")
a=[]

for i in range(len(n)):
    if(n[i]=='0'):
        a.append(1)
    else:
        a.append(0)
    print(a[i],end="")
