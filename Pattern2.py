#Patterns Number

n = int(input("Enter Rows : "))
#n = 5
for i in range(1,n+1):
    for j in range(0,i):
        print(i,end="")
    print("")
