#Sum of digits using function

def sum_of_digits(num):
    rem = 0
    sum = 0
    for i in range(0,num):
        rem = num%10
        sum = sum + rem
        num//=10
    return sum


n = int(input("Enter Number : "))
print(sum_of_digits(n))
