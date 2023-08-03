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
        if i == 5:
            stars -= 1
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


def print_pyramid(rows):
    outer_spaces = rows//2
    inner_spaces = 0
    for i in range(rows):
        j = 1
        while j <= outer_spaces:
            print("    ", end = "")
            j += 1
        print("*", end = "")
        k = 1
        while k <= inner_spaces:
            print("    ", end = "")
            k += 1
        if i != 0 and i != rows-1:
            print("*")
        else:
            print()
        if i < rows//2:
            outer_spaces -= 1
            inner_spaces += 2
        else:
            outer_spaces += 1
            inner_spaces -= 2
        print()
        # print(print_pyramid(5))
print_pyramid(5)

def print_pyramid(rows):
    outer_spaces = rows//2
    inner_spaces = 0
    for i in range(rows):
        j = 1
        while j <= outer_spaces:
            print(" ", end = "")
            j += 1
        print("*", end = "")
        k = 1
        while k <= inner_spaces:
            print(" ", end = "")
            k += 1
        if i != 0 and i != rows-1:
            print("*")
        else:
            print()
        if i < rows//2:
            outer_spaces -= 1
            inner_spaces += 2
        else:
            outer_spaces += 1
            inner_spaces -= 2
        # print(print_pyramid(5))
print_pyramid(5)

class Person:
    def __init__(self, name):
        self.name = name 
        
    def talk(self):
        print("talk")
        
john = Person("John Smith")
print(john.name)
john.talk()

def print_pyramid(rows):
    spaces = rows//2
    stars = 1
    for i in range(rows):
        j = 1
        while j <= spaces:
            print(" ", end = "")
            j += 1
        print("*", end = "")
        k = 1
        while k <= stars:
            print("*", end = "")
            k += 1
        if i <= rows//2:
            spaces += 0
            stars += 1
        else:
            spaces += 0
            stars -= 1
            print()
        # print(print_pyramid(5))
print_pyramid(5)


def print_pyramid(rows):
    stars = 1
    spaces = 2
    for i in range(rows):
        if i == rows//2:
            print("**",end = "")
        else:
            p = 1
            while p <= spaces:
                print(" ", end = "")
                p += 1
        j = 1
        while j <= stars:
            print("*", end = "")
            j += 1
        if i < rows//2:
            stars += 1
            spaces += 0
        else:
            stars -= 1
            spaces += 0
        # print(print_pyramid(5))
        print()
print_pyramid(500)

def print_pyramid(rows):
    stars = 1
    up_outer_spaces = 1
    down_outer_spaces = rows//2
    inner_spaces = 3
    # inner_spaces = 3
    for i in range(rows):
        if i == 0:
            print(rows*"*")
        else:
            if i < rows//2:
                p = 1
                while p <= up_outer_spaces:
                    print(" ", end = "")
                    p += 1
                j = 1
                while j <= stars:
                    print("*", end = "")
                    j += 1
                k = 1
                while k <= inner_spaces:
                    print(" ", end = "")
                    k += 1
                print('*')
                up_outer_spaces += 1
                inner_spaces -= 2
            else:
                p = 1
                while p <= down_outer_spaces:
                    print(" ", end = "")
                    p += 1
                j = 1
                while j <= stars:
                    print("*", end = "")
                    j += 1
                stars += 2
                down_outer_spaces -= 1
            # print(print_pyramid(5))
                print()
print_pyramid(7)

 










