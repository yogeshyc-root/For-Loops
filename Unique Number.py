# Unique Number Using 1,2,3,4 and count total number of Unique Numbers
a = []

for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if(i!=j and j!=k and k!=i):
                a.append(i)
                a.append(j)
                a.append(k)
                print(i,j,k)
print("Unique Number count is :",len(a)//3)


"""
#Unique Number Using n numbers and count total number of Unique Numbers

n = int(input("Enter Number : "))
a = []

for i in range(1,n):
    for j in range(1,n):
        for k in range(1,n):
            if(i!=j and j!=k and k!=i):
                a.append(i)
                a.append(j)
                a.append(k)
                print(i,j,k)
print("Unique Number count is :",len(a)/n)
"""