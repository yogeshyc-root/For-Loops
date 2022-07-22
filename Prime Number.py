a = int(input("Number"))
n = int(a**0.5)
flag = False

if(a>1):
    for i in range(2,n+1):
        if(a%i==0):
            print("Not Prime")
            flag = True
            break
elif(a==1):
    print("1 is Prime")
else:
    print("Enter Number above 1 or Positive Integer Only")
if(not flag):
    print("Prime")
