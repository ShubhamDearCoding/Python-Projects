def print_pyramid(rows):
    outer_spaces = rows//2
    inner_spaces = 0
    for i in range(rows):
        j = 1
        while j <= outer_spaces:
            print(" ", end = "")
            j += 1
        print("*", end = "")
        k = 1
        while k <= inner_spaces:
            print(" ", end = "")
            k += 1
        if i != 0 and i != rows-1:
            print("*")
        else:
            print()
        if i < rows//2:
            outer_spaces -= 1
            inner_spaces += 2
        else:
            outer_spaces += 1
            inner_spaces -= 2
        # print(print_pyramid(5))
print_pyramid(5)