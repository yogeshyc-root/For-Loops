#Reverse a String

n = input("Enter String : ")

for i in range(len(n)-1,-1,-1):
    print(n[i],end="")
