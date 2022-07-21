a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]


for i in range(0,len(a)):
    if(a[i]==1):
        print("Prime",a[i])
    elif(a[i]<1):
        print("Enter Positive")
    else:
        b = int(a[i] ** 0.5)
        flag = False
        for j in range(2,b+1):
            if(a[i]%j==0):
                flag = True
                print("Not Prime",a[i])
                break
        if(not flag):
            print("Prime",a[i])
