number = int(input("Enter any number "))
# if only number // 1 and number // number: 
count = 2
while count < number:
    if number%count == 0:
        break     
    count  += 1
if count == number:
    print("prime number")       
else:
    print("not a prime number")