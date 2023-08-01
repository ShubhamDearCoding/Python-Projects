Q.write a python program to print 10 multiples of a number , also prints sum of all the multiples.
number = int(input("enter a number "))
count = 2
sum = 0
while count < 10:
    multiple = count*number
    print(multiple)
    sum += multiple
    count += 1
print(sum)


number = int(input("enter a number "))
factorial = 1
count = 1
while count <= number:
    factorial = factorial*count
    # factorial *= count
    count += 1      
print(factorial)
    

    






