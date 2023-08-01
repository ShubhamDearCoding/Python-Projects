a = "hello"
print(a*3)

a = [3,4]
print(a*3)

# write a program to find the prime numbers in a given range using nested loop

# write a python program to reverse a number using while loop

def reverse_number(num):
    reversed_num = 0
    while num > 0:
        digit = num%10
        reversed_num = reversed_num*10 + digit
        num//= 10
    return reversed_num
print(reverse_number(45))

# write a program to find the gcd of two numbers using euclidian algorithm in a loop 
def gcd(a,b):
    while b != 0:
        a,b = b,a%b
    return a
print(gcd(3,6))
# write a program to find sum of n terms of a fibbonacci seqence using a for loop
# 0,1,2,3,4,5,6,7,8,9
def fibonacci(n):
        fib_sequence = [0,1]
        for i in range (2,n):
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
print(fibonacci(5))



# write program to find factorial of a number using while loop
def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result
print(factorial(4))
