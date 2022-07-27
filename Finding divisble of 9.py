#Number & sum of all integers divisible by 9 b/w 100-200

sum = 0

for i in range(100,200):
    if(i%9==0):
        print(i)
        sum = sum+i
print("Sum is ",sum)
