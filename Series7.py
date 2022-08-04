#Sum of Series [ 1+x+x^2/2!+x^3/3!+....]

x = int(input("Enter the X value : "))
n = int(input("Enter the limit : "))

sum = 1 + x
sum1 = 1
for i in range(2,n):
    for j in range(2,i+1):
        sum1= sum1 * j
    sum += ((x**i)/sum1)
    sum1 = 1
print(sum)
