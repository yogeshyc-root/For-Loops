a = input("Enter String :")
b = input("Enter Finding Substring or Letter:")

flag = False

count = 0

j = 0

for i in range(0,len(a)):
    if(a[i]==b[j]):
        j+=1
    else:
        j=0
    if(j == len(b)):
        count+=1
        j = 0
print(count)
