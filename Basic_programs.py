        # PROBLEM 1

# a = int(input("enter a "))
# b = int(input("enter b "))
# print(a+b)

        # PROBLEM 2

# a = 3
# b = 4
# print(max(a,b))

        # PROBLEM 3

# a = int(input("enter a "))
# fact = 1
# if a < 0:
#    print(" Factorial does not exist for negative numbers")
# elif a == 0:
#    print("The factorial of 0 is 1")
# else:
#    for i in range(1,a + 1):
#        fact = fact*i
#    print("The factorial of",a,"is",fact)

        # PROBLEM 4

# P = int(input("enter P "))
# T = int(input("enter T "))
# R = int(input("enter R "))
# simple_interest = int((P * R * T)/ 100)
# print(simple_interest)

        # PROBLEM 5

# P = int(input("enter P "))
# r = int(input("enter r "))
# T = int(input("enter T "))
# Compound_Interest = int(P*(1 + r/100)**T)
# print(Compound_Interest)

        # PROBLEM 6

# num = int(input("Enter a number: "))
# sum = 0
# temp = num

# while temp > 0:
#    digit = temp % 10
#    sum += digit ** 3
#    temp //= 10

# if num == sum:
#     print(num,"is an Armstrong number")
# else:
#     print(num,"is not an Armstrong number")

            # PROBLEM 7

# P = 3.14
# r = 4
# area = 3.14 * r * r
# print(area)

            # PROBLEM 8

# start = 11
# end = 25

# for i in range(start, end+1):
#     if i>1:
#         for j in range(2,i):
#             if(i % j==0):
#                 break
#         else:
#             print(i)

            # PROBLEM 9

# number = int(input("Enter a number"))
# def prime_check(n):
#     for i in range(2,int(n/2)+1):
#         if(n%i) ==0:
#             print(f"{n} is not prime")
#             break
#     else:
#         print(f"{n} is prime")
#
# prime_check(number)

            # PROBLEM 10

# n = int(input("Enter the value of 'n': "))
# a = 0
# b = 1
# sum = 0
# count = 1
# print("Fibonacci Series: ", end = " ")
# while(count <= n):
#     print(sum , end =" ")
#     count += 1
#     a = b
#     b = sum
#     sum = a+b

           # PROBLEM 11

# n=int(input("Enter the number: "))
# c=0
# a=1
# b=1
# if n==0 or n==1:
#     print("Yes")
# else:
#     while c<n:
#         c=a+b
#         b=a
#         a=c
#     if c==n:
#         print("Yes")
#     else:
#         print("No")

            # PROBLEM 12

# def find(k, n):
#     f1 = 0
#     f2 = 1
#     i = 2
#     while i != 0:
#         f3 = f1 + f2
#         f1 = f2;
#         f2 = f3;
#         if f2 % k == 0:
#             return n * i
#         i += 1
#     return
# n = 5
# k = 4
# print("Position of n\ 'th multiple of k in""Fibonacci Series is: ", find(k,n))


# def iterative_fibonacci(n):
#     previous, current = 0 , 1
#     for _ in range(2,n):
#         next_term = current + previous
#         previous = current
#         current = next_term
#     return current

# print(iterative_fibonacci(12))

                # PROBLEM 13

# c = str(input('Enter the character in c : '))
# print("The ASCII value of '" + c + "' is", ord(c))


                # PROBLEM 14


# def square_sum(n):
#     sum = 0
#     for i in range(1,n+1):
#         sum = sum + (i * i)

    # return sum
# n = 4
# print(square_sum(n))

                # PROBLEM 15


# def cube_sum(n):
#     sum = 0
#     for i in range(1,n+1):
#         sum = sum + (i * i * i)

    # return sum
# n = 4
# print(cube_sum(n))







