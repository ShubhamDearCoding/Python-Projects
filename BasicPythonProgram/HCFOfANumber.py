number = int(input("enter a number "))
number_2 = int(input("enter a number "))
count = 0
hcf = 1

# while count <= 100: 
while count < number or count < number_2: 
    count += 1
    if number*count == number_2*count :
        if count > hcf:
            hcf = count
print(hcf)

number = int(input("enter a number "))
number_2 = int(input("enter a number "))
count = 0
hcf = 1

# while count <= 100: 
while count < number or count < number_2: 
    count += 1
    if number%count == 0 and number_2%count == 0:
        if count > hcf:
            hcf = count
print(hcf)