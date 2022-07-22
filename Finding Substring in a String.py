a = input("Enter String :")
b = input("Enter Finding Substring or Letter:")

flag = False

count = 0

temp = []

for i in range(0,len(a)):
    if(b[0]==a[i]):
        for j in range(0,len(b)):
            if(a[i]==b[j]) and (i+len(b)<len(b)):
                flag = True
                temp.append(a[i])
                i+=1
            else:
                flag = False
                break
        if(flag):
            count+=1
   
if (not flag):
    print("Not Found")
print(temp,count)
