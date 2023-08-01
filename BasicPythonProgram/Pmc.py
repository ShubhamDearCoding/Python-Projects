count =0
while(True):
    if count%3 == 0:
        print(count,end = " ")
    if(count>15):
        break
    count+= 1

3
6
9
12
15















Q1
create a Person class with the following attributes :
name and age. implement a method greet() that prints a greeting message including the person's name
Ans1

class Person:
    def __init__ (self, name,age):
        self.name = name
        self.age = age 
        
    def greet(self):
        print("greet")

shubham = Person('Shubham Jha',20)
print(shubham.age)
shubham.greet()

# class Person:
#     def greet(self):
#         print("greet")

# person1 = Person()
# person1.name = "shubham jha"
# person1.age = 20
# print(person1.age)
# person1.greet()                                                                                                          

Q2
create a class Rectangle that represents a rectangle. it should have attributes width and height implements method to calculate area and parameter of the rectangle

class Rectangle:
    def __init__ (self, width, height):
        self.width = width
        self.height = height
        
    
    def area(self):
        print("area:", (self.width * self.height))

    def parameter(self):
        print("parameter:", 2 * (self.width + self.height))

Rectangle1 = Rectangle(10,20)
Rectangle1.area()
Rectangle1.parameter()
# self contains the address of  the current object


Q3
write a BankAccount class
 with attributes account_number, account_holder and balance.
implement methods deposit(amount) and withdrawl(amount) to deposit and withdrawl funds, respectively.

class BankAccount:
    def __init__ (self, account_number, account_holder, balance):
        self.account_number = account_number 
        self.account_holder = account_holder 
        self.balance = balance
      
 
    def deposit(self, amount):
        print('you deposited:', amount)
        balance = self.balance + amount 
        print("current balance: ",balance)

    def withdrawl(self, amount):
        print("current balance: ",self.balance - amount)

shubham_bank_account = BankAccount(10, 'shubham', 30)
shubham_bank_account.deposit(100)
print(shubham_bank_account.balance)

Q4
create Car class with attributes make, model and year. implement a method display_info()that prints the car information.

class Car:
    def __init__ (self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
    
    def display_info(self):
        print('display_info')

carinfo = Car(10, 'shubham', 30)
print(carinfo.make)

Q5
implement a class circle with attribute radius. Add methods to calculate the area and circumference of the circle.

class Circle:
    def __init__ (self, radius):
        self.radius = radius
        
        

    def area(self):
        print("area:", (3.14 * self.radius * self.radius))

    def cicumference(self):
        print("cicumference:", (2 * 3.14 * self.radius))

Circle1 = Circle(10)
Circle1.cicumference()
Circle1.area()

Q6
create a Student class with attributes name, age and a list grades. Implement a method add_grade(grade) to add grades to the students list, and another method get average grade to calculate and return the average grade.

class Student:
    def __init__ (self, name, age, grades,a,b):
        self.name = name
        self.age = age
        self.grades = grades
        self.a = a
        self.b = b
        grades = [a,b]

    def add_grades(self):
        print("total:", self.a + self.b)

    def avg_grades(self):
        print("avg_grades:", (self.a + self.b)/4)

Student1 = Student('shubham', 18, 'A', 2, 4)
Student1.add_grades()
Student1.avg_grades()


Q7
write a Book class with attributes title, author and publication year. Implement a method display_info() to print all the book information.

class Book:
    def __init__ (self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year


    def display_info(self):
        print('display_info')

Book_info = Book(10, 'shubham', 30)
print(Book_info.author)

Q8
Create a class "Bank" that stores multiple 'Bank account' objects. Implement a method 'total_balance()' to calculate the total balamce of all accounts in the bank.

class Bank:
    def __init__ (self, shubham, jha):
        self.shubham = shubham
        self.jha = jha 
     
      
    def total_balance(self):
        print('total balance:', shubham + jha)

Bank1 = Bank(10, 30)
print(Bank1.shubham)

Q9
Write a 'Triaingle' class with attributes 'side1', 'side2', and 'side3'. Implement a method 'is_equivalent()' that returns True if the triangle is equilateral(all sides equal) and false otherwise.

class Triangle:
    def __init__ (self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3 
     
      
    def is_equivalent(self):
        print('is equivalent')

side1 = Triangle(10, 30, 20)
side2 = Triangle(10, 30, 20)
side3 = Triangle(10, 30, 20)
if side1 == side2 == side3:
    print(True)
else:
    print(False)


Q10
Create a 'Employee' class with attributes 'name =', 'position', and 'salary'. Implement a method 'claculate_bonus()' that calculates and return a 10% bonus on the salary.

class Employee:
    def __init__ (self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
      
 
    def claculate_bonus(self):
        print('bonus given:', bonus)
        salary = self.salary + bonus
        print("total salary: ",bonus)

Employee1 = Employee(10, 'shubham', 30)
print(Employee1.salary)











# inheritance
class Dog(Mammal):
    def bark(self):
        print("bark")

class Cat(Mammal):
    def be annoying(self):
        print("annoying")

cat1 = Cat()
cat1.

dog1 = Dog()
dog1.walk()






class Person:
    def __init__ (self, name):
        self.name = name
        

    def talk(self):
        print("talk")

shubham = Person('Shubham Jha')
print(shubham.name)
shubham.talk()
 









# constructor

class Point:
    def __init__ (self, x, y):
            self.x = x
            self.y = y

point = Point(10,20)
print(point.x)


class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")

    def add(self):
       print("add")

point1 = Point()
# creating attribute x on point 1 object 
point1.x = 10
point1.y = 20
print(point1.x)
# calling draw method on/of point1 object
point1.draw()

point3 = Point()
point3.x = 30
point3.y =40
print(point3.y)
point3.add()

# 10
# draw
# 40
# add




fruits = ["apple", "banana", "cherry","mango","kiwi"]
fruit = 0
while fruit < len(fruits):
    print(fruits[fruit])
    fruit += 1




fruits = ["apple", "banana", "cherry"]
fruit = 0
while fruit < 3:
    print(fruits[fruit])
    fruit += 1







fruits = ["apple", "banana", "cherry"]
print("apple" in fruits)
print("kiwi" in fruits)
for _ in fruits:
    print("happy")

fruits = ["apple", "banana", "cherry"]
for _ in fruits:
    print(fruit)
# NameError: name 'fruit' is not defined. Did you mean: 'fruits'?



a = [1, 2, 3]
a = tuple(a)
a[0] = 2
print(a)
# TypeError: 'tuple' object does not support item assignment

print(type(5/2))
# Output = 2.5
print(type(5//2))
# Output = 2

print(5/2)
# Output = 2.5
print(5//2)
# Output = 2