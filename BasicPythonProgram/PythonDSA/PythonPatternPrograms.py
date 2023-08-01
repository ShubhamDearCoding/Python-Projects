def print_pyramid(rows):
    for i in range(rows):
        for j in range(rows -i -1):
            print(" ", end = "")
        for k in range(2*i +1):
            print("*", end = "")
        # print(print_pyramid(5))
        print()
print_pyramid(5)

def print_pyramid(rows):
    for i in range(rows):
        for j in range(0):
            print(" ", end = "")
        for k in range(rows - i):
            print("*", end = "")
        # print(print_pyramid(5))
        print()
print_pyramid(5)

def print_pyramid(rows):
    for i in range(rows):
        for j in range(rows -i -1):
            print(" ", end = "")
        for k in range(i +1):
            print("*", end = "")
        # print(print_pyramid(5))
        print()
print_pyramid(5)

def print_pyramid(rows):
    for i in range(rows):
        for j in range(i):
            print(" ", end = "")
        for k in range(rows - i):
            print("*", end = "")
        # print(print_pyramid(5))
        print()
print_pyramid(5)

def print_pyramid(rows):
    for i in range(rows):
        for j in range(i):
            print(" ", end = "")
        print("*", end = "")
        # print(print_pyramid(5))
        print()
print_pyramid(5)

def print_pyramid(rows):
    for i in range(rows):
        for j in range(rows -i -1):
            print(" ", end = "")
        print("*", end = "")
        # print(print_pyramid(5))
        print()
print_pyramid(5)

def print_pyramid(rows):
    for i in range(rows):
        if i < 5//2:
            for j in range(i):
                print(" ", end = "")
            print("*", end = "")
            for j in range(rows//2 +1 - 2*i):
                print(" ", end = "")
            print("*", end = "")
        if i > 5//2:
            for j in range(rows -i -1):
                print(" ", end = "")
            space = 1
            for j in range(rows//2 +1 - 2*i):
                print(" ", end = "")
                space += 2 
            print("*", end = "")     
        # print(print_pyramid(5))
            print()
print_pyramid(5)

def print_pyramid(rows):
    num = 1
    num2 = 0
    for i in range(rows):
        for k in range(i + 1):
            print(num, ' ', end = "")
            num += num2
        # print(print_pyramid(5))
        print()
print_pyramid(4)

def print_pyramid(rows):
    for i in range(rows):
        for j in range(2):
            print(" ", end = "")
        for k in range(i + 1):
            print("*", end = "")
        # print(print_pyramid(5))
        print()
print_pyramid(5)

def print_pyramid(rows):
    for i in range(rows):
        for j in range(0):
            print(" ", end = "")
        for k in range(1):
            print("*", end = "")
        # print(print_pyramid(5))
        print()
print_pyramid(100)

def print_pyramid(rows):
    for i in range(rows):
        for j in range(0):
            print(" ", end = "")
        for k in range(i +1):
            print("*", end = "")
        # print(print_pyramid(5))
        print()
print_pyramid(5)

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
    
def print_pyramid(rows):
    stars = 1
    spaces = 2
    for i in range(rows):
        j = 1
        while j <= spaces:
            print(" ", end = "")
            j += 1
        k = 1
        while k <= stars:
            print("*", end = "")
            k += 1
        if i < rows//2:
            stars += 2
            spaces -= 1
        else:
            stars -= 2
            spaces += 1
        # print(print_pyramid(5))
        print()
print_pyramid(5)


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
    
def print_pyramid(rows):
    stars = 1
    spaces = 2
    for i in range(rows):
        j = 1
        while j <= spaces:
            print(" ", end = "")
            j += 1
        k = 1
        while k <= stars:
            print("*", end = "")
            k += 1
        if i < rows//2:
            stars += 2
            spaces -= 1
        else:
            stars -= 2
            spaces += 1
        # print(print_pyramid(5))
        print()
print_pyramid(5)

def print_pyramid(rows):
    stars = 3
    spaces = 2
    for i in range(rows):
        p = 1
        while p <= stars:
            print("*", end = "")
            p += 1
        j = 1
        while j <= spaces:
            print(" ", end = "")
            j += 1
        k = 1
        while k <= stars:
            print("*", end = "")
            k += 1
        if i < rows//2:
            stars -= 1
            spaces += 2
        else:
            stars += 1
            spaces -= 2
        # print(print_pyramid(5))
        print()
print_pyramid(5)


def print_pyramid(rows):
    stars = 1
    spaces = 2
    for i in range(rows):
        p = 1
        while p <= stars:
            print("*", end = "")
            p += 1
        j = 1
        while j <= spaces:
            print(" ", end = "")
            j += 1
        k = 1
        while k <= stars:
            print("*", end = "")
            k += 1
        if i < rows//2:
            stars += 1
            spaces -= 1
        else:
            stars += 1
            spaces -= 1
        # print(print_pyramid(5))
        print()
print_pyramid(5)


def print_pyramid(rows):
    stars = 1
    spaces = 5
    for i in range(rows):
        p = 1
        while p <= stars:
            print("*", end = "")
            p += 1
        j = 1
        while j <= spaces:
            print(" ", end = "")
            j += 1
        k = 1
        while k <= stars:
            print("*", end = "")
            k += 1
        if i < 2//2:
            stars += 0
            spaces -= 0
        else:
            stars += 1
            spaces -= 2
        # print(print_pyramid(5))
        print()
print_pyramid(5)


    





