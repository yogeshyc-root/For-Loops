#Multiplication Table

n = int(input("Enter Table Number"))

for i in range(1,n+1):
    for j in range(1,101):
        print(j,"x",i,"=",i*j)
    print("--------------")
