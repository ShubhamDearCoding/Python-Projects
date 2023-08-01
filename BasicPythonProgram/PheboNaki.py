# Write a Python Program to Swap Two Numbers
# e.g. 
# before swapping: a = 4, b = 8
# after swapping: a = 8, b = 4
# Fibonacci sequence
# print first n terms of the fibbonacci sequence

num_of_terms = int(input("enter number of terms "))
i = 0
first_term = 0
second_term = 1
print(first_term, second_term, end=" ")
while i < num_of_terms - 2:
    third_term = first_term + second_term 
    first_term = second_term 
    second_term = third_term
    print(third_term, end=" ")
    i += 1

count = 1
mount = 0
bount = 1 
while count < 100:
    if count + mount == bount:
        print(count+bount)
        count += 1
        mount += 1
        bount += 1
        



count1 = 0
count2 = 1
count3 = 1
while count1 + count2 == count3:
    print(count2 + count3)
    count1 += 1
    count2 += 1



count = 0
while count < 100:
    print(count + count + 1)
    count += 1