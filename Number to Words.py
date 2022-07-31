#Input any number & print it in words

n = int(input("Enter Number : "))
rem = 0
a = []

for i in range(0,n):
    rem = n%10

    if(rem==0):
        a.append("Zero")
    elif(rem==1):
        a.append("One")
    elif(rem==2):
        a.append("Two")
    elif(rem==3):
        a.append("Three")
    elif(rem==4):
        a.append("Four")
    elif(rem==5):
        a.append("Five")
    elif(rem==6):
        a.append("Six")
    elif(rem==7):
        a.append("Seven")
    elif(rem==8):
        a.append("Eight")
    elif(rem==9):
        a.append("Nine")
    else:
        break
    n//=10
    if(n==0):
        break
for i in range(len(a)-1,-1,-1):
    print(a[i],end=" ")


