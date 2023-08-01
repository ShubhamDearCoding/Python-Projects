side_1 = int(input("enter a number "))
side_2 = int(input("enter a number "))
side_3 = int(input("enter a number "))
if side_1 + side_2 < side_3 or side_2 + side_3 < side_1 or side_3 + side_1 < side_2:
    print("not valid")
else:
    print("Valid")

# how to give more than one input using input function, in the same line 
# input function in python 