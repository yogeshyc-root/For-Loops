#Binary to Octal

n = input("Enter Number : ")
sum = 0
j = 0
n1 = len(n)-1

for i in range(n1,-1,-1):
    sum = int(n[int(i)]) * (2**int(j)) + sum
    j+=1