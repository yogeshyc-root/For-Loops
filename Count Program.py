# Count of letters,spaces,numbers and other characters

n = input("Enter String : ")
letter = 0
space = 0
number = 0
count = 0

for i in range(0,len(n)):
    if(n[i]>='a' and n[i]<='z') or (n[i]>='A' and n[i]<='Z'):
        letter+=1
    elif(n[i]==' '):
        space+=1
    elif(n[i]>='0' and n[i]<='9'):
        number+=1
    else:
        count+=1

print("Number of Chracters          : ",len(n))
print("Number of Alphabetes         : ",letter)
print("Number of Numbers            : ",number)
print("Number of Spaces             : ",space)
print("Number of Other Characters   : ",count)