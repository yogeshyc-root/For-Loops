#Frequency of a Number in Given Number

a = [0,1,2,3,4,5,6,7,8,9]
n = input("Enter Number : ")

for i in range(0,len(a)):
    count = 0
    for j in range(0,len(n)):
        if(int(n[int(j)])==a[i]):
            count+=1
    print(a[i],"----->",count)
