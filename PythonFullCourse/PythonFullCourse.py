print("shubham jha")
print('*' * 10)

name = "John Smith" 
age = 20
patient = "new"
print(name, age, patient)

name = input("what is your name? ")
print('hi' + name)

name = input("what is your name? ")
colour = input('what is your fav colour? ')
print(name +" likes "  + colour)
 
birth_year = int(input("birth_year : "))
age = 2023 - birth_year
print(type(age))
print(age)

weight = int(input("what is your wieght ? "))
print(weight * 1000)

course = 'python for "beginners"'
print(course)

course = '''
hi john,

here is our first email to you.

'''
print(course)

course = 'pyhton programs for begginners '
print(course[0])


course = 'pyhton programs for begginners '
print(course[-2])


course = 'pyhton programs for begginners '
print(course[0:])

course = 'python for beginners'
print(course.replace('beginners', 'absolute beginners '))

course = 'python for beginners'
print('python' in course)

course = 'python for beginners'
len()
course.upper()
course.lower()
course.title()
course.find()
course.replace()
'.....' in course

print(10 / 3)
print(10 // 3)
print(10 ** 3)
print(10 / 3)
print(10 % 3)

x = 10
x += 3
print(x)

x = 2.9
print(round(x))


x = 2.9
print(abs(-x))

import math 
print(math.ceil(2.9))

import math 
print(math.floor(2.9))

is_hot = True
if is_hot:
    print('its a hot day')
    print("Drink plenty of water")
else:
    print("its a cold day")
    print("wear worm clothes")
print("enjoy your day")

is_good = True
if is_good:
    down_payment = 0.1 * 1000000
else: 
    down_payment = 0.2 * 1000000
print(f" down payment : ${down_payment}")

has_high_income = False
has_good_credit = True

if has_high_income and has_good_credit:
    print("eligilble for loan")
    
name = "shubh"
if len(name) < 3:
    print("bad word")
elif len(name) > 50:
    print("decent word") 
else:
    print("good word")
    
weight = int(input('Weight: '))
unit = input('(L)bs or (K)g: ')
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")

i = 1
while i <= 5:
    print(i)
    i = i + 1
print("Done")

i = 1
while i <= 5:
    print('*' * i)
    i = i + 1
print("Done")

secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    Guess = int(input('Guess: '))
    guess_count+= 1
    if Guess == secret_number:
        print('You won!')
        break
else:
    print('You failed')

start = 0
stop = 0
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    Guess = (input('Guess: '))
    if Guess == stop:
        print('stop the car')
    elif Guess == start:
        print('start the car')
else:
    print('i dont understand that')
    
command = ""
while command != "quit":
    command = input("> ").lower()
    if command == "start":
        print("Car started..")
    elif command == "stop":
        print("Car stopped...")
    elif command == "help":
        print("""
              start - to start the car 
              stop - to stop the car 
              quit - to quit 
              """)
    else:
        print("Sorry, I dont understand that")
        
prices = [10, 20, 30]

for item in ["mosh", "sarah", "john"]:
    print(item)

total = 0
for price in prices:
    total += price
print(f"Total: {total}")

for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')
        
for x in range(4):
    for y in range(3):
        print(f'({x},{y})')
        
numbers = [5,2,5,2,2]
for x_count in numbers:
    print('x' * x_count)
    
numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output) 
    
numbers = [1,2,3,4,5]
max = numbers[0]

for number in numbers:
    if number > max:
        max = number
print(max)

matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
]
for row in matrix:
    for item in row:
        print(item)
        
numbers = [5, 4, 3, 2, 1]
numbers.append(20)
print(numbers)

numbers = [5, 4, 3, 2, 1]
numbers.append(20)
print(numbers)

numbers = [5, 4, 3, 2, 1]
numbers.insert(2, 20)
print(numbers)

numbers = [5, 4, 3, 2, 1]
numbers.remove(2, 20)
print(numbers)

numbers = [5, 4, 3, 2, 1]
numbers.remove(5)
print(numbers)

numbers = [5, 4, 3, 2, 1]
numbers.clear()
print(numbers)

numbers = [5, 4, 3, 2, 1]
numbers.pop()
print(numbers)

numbers = [5, 4, 3, 2, 1]
print(numbers.index(5))

numbers = [5, 4, 3, 2, 1]
print(numbers.count(5))


numbers = [5, 4, 3, 2, 1]
numbers.sort()
print(numbers)

numbers = [5, 4, 3, 2, 1]
numbers.sort()
numbers.reverse()
print(numbers)

numbers = [5, 4, 3, 2, 1]
numbers2 = numbers.copy()
numbers.append(10)

print(numbers2)

numbers = [5, 4, 3, 5, 2, 1]
numbers.sort()
print(numbers)

numbers = [5, 4, 3, 5, 2, 1]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

numbers = (5, 4, 3, 2, 1)
numbers[0] = 10
print(numbers[0])

coordinates = (1, 2, 3)
x, y, z = coordinates
print(y)

customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
customer["name"] = 'jack smith'
print(customer["name"])

phone = input("Phone: ")
digits_mapping = {
    "1" : "one",
    "2" : "two",
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)

message = input("> ")
words = message.split(' ')
emojis = {
    ":)": "😁",
    ":(": "😢"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)

def greet_user():
    print('hi there! ')
    print('welcome aboard ')
    

print("start")
greet_user()
print("finish")

def greet_user(name):
    print(f'hi {name}! ')
    print('welcome aboard ')
    

print("start")
greet_user("john")
greet_user("mary")
print("finish")

def greet_user(first_name, last_name):
    print(f'hi {first_name},{last_name}! ')
    print('welcome aboard ')
    

print("start")
greet_user("john", "smith")
print("finish")

def square(number):
    print(number * number)


print(square(3))

def emoji converter(message):
    words = message.split(' ')
    emojis = {
        ":)": "😁",
        ":(": "😢"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output

message = input(">")
print(emoji_converter(message))

try:
    age = int(input('Age: '))
    income = 20000
    risk = income/age 
    print(age)
except ValueError:
    print('Invalid value')

try:
    age = int(input('Age: '))
    income = 20000
    risk = income/age 
    print(age)
except ZeroDivisionError:
    print('Age cannot be 0.')
except ValueError:
    print('Invalid value')

class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")

point1 = point()
point1.x = 10
point1.y = 20
print(point1.x)
point.draw()

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point = Point(10, 20)
point.x = 10
print(point.x)







        

        
    
    
    