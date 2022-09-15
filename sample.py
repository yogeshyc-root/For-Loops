def findPosition(k, n):
    f1 = 0
    f2 = 1
    i = 2
    while i!=0:
        f3 = f1 + f2
        f1 = f2
        f2 = f3

        if f2 % k == 0:
            print("---->",i)
            return n * i
        i+=1
        print(i)
n = 5
k = 6

print(findPosition(k,n))