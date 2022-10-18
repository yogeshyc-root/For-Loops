# # Python Program to find position of n\'th multiple of a number k in Fibonacci Series


# def findPosition(k, n):
#     f1 = 0
#     f2 = 1
#     i = 2
#     while i!=0:
#         f3 = f1 + f2
#         f1 = f2
#         f2 = f3

#         if f2 % k == 0:
#             print("---->",i)
#             return n * i
#         i+=1
#         print(i)
# n = 5
# k = 4

# print(findPosition(k,n))

# for i in range(0,5):
#     for j in range(0,5):
#         print("* ",end="")
#     print()



n = 5
num = 10
for i in range(0,n):
    num = 10
    for j in range(i):
        print(num,end=" ")
        num -=2
    print('')