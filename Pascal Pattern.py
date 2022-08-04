temp = [0,1,2,1,0]
temp1=[]
# print(1)
for i in range(0,len(temp)-1):
    # temp1.append(1)
    temp1.append(temp[i]+temp[i+1])
    # temp1.append(temp)
print(temp1)
temp = temp1
temp1 = []
