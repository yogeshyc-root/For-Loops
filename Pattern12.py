n = 5
temp = [1,1]
temp1=[]
for j in range(1,n+1):
    temp1.append(1)
    for i in range(1,len(temp)):
        temp1.append(temp[i-1]+temp[i])
    temp1.append(1)
    print(temp1)
    temp = temp1
    temp1 = []
