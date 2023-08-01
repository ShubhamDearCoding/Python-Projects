number = int(input("enter a number "))
number_2 = int(input("enter a number "))
count = 0
lcm = 1
a = 1
b = 1

# while count <= 100: 
while : count < number or count < number_2:
    count += 1
    if count < number or count < number_2:
        if a == b:
            lcm = count
print(lcm)