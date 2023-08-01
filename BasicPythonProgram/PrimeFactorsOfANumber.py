number = int(input("enter a number "))
count = 2
while count <= number:
    count += 1
    if number%count == 0:
        print(count)
    else:
        continue
                     