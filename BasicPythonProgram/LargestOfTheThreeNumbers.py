def find_largest_number(num1, num2, num3):
    largest = num1
    if num2 > largest:
        largest = num2
    if num3 > largest:
        largest = num3
    return largest

# Example usage
num1 = 6
num2 = 8
num3 = 9
largest_number = find_largest_number(num1, num2, num3)
print("The largest number is:", largest_number)

