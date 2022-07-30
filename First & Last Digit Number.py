#First & Last digit of a number

n = input("Enter Input : ")
a = len(n)-1
for i in range(0,len(n)):
    if(n[0] or n[a]):
        print(n[0])
        print(n[a])
        break
