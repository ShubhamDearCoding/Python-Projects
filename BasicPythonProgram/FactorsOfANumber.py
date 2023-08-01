import math 
number = int(input("enter a number "))
print("fators of", number, ":")
count = 0
while count <= math.sqrt(number):
    count += 1
    if number%count == 0:
        print(count, number//count) 
    else:
        continue   

number = int(input("enter a number "))
count = 0
while count <= number:
    count += 1
    if number%count == 0:
        print(count)  
    else:
        continue
    
number = int(input("enter a number "))
count = 0
while count <= 1000000:
    count += 1
    if number%count == 0:
        print(count)  
    else:
        continue   
    
     