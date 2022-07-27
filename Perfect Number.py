#Perfect Number between 1 to 500

for i in range(1,500):
    sum = 0
    for j in range(1,i):
        if(i%j==0):
            sum = sum+j
    if(sum==i):
        print(i,"Perfect Number")
