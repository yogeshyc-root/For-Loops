# Input positive integers to process count maximum, minimum, and average or terminate the process with -1

n = int(input("How many numbers do you want to process(+ve integers only) : "))
a = []
sum = 0
if(n==-1):
    print("Process Terminated!")
elif(n>0):
    for i in range(0,n):
        print("Enter Number ",i+1,end=" : ")
        a.append(int(input("")))
    for i in range(0,len(a)):
        sum = sum + a[i]
    avg = sum/len(a)
    max = max(a)
    min = min(a)
else:
    print("Enter Positive Integers!")

print("Maximum is :",max)
print("Minimum is :",min)
print("Average is :",avg)
