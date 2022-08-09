#Sum of Series  1.2 + 2.3 + 3.4 + 4.5 + 5.6 + 6.7 + 7.8 + 8.9 + 9.1 + 10.11 

n = int(input("Enter The Number : "))
j = 1
sum = 0
for i in range(1,n+1):
    j+=1
    sum = (i+(j/10)) + sum
    print("------->",sum)
print(sum)