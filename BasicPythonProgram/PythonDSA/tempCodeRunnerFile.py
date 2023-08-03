def print_pyramid(rows):
    stars = 1
    up_outer_spaces = 1
    down_outer_spaces = rows//2
    inner_spaces = 3
    # inner_spaces = 3
    for i in range(rows):
        if i == 0:
            print(rows*"*")
        else:
            if i < rows//2:
                p = 1
                while p <= up_outer_spaces:
                    print(" ", end = "")
                    p += 1
                j = 1
                while j <= stars:
                    print("*", end = "")
                    j += 1
                k = 1
                while k <= inner_spaces:
                    print(" ", end = "")
                    k += 1
                print('*')
                up_outer_spaces += 1
                inner_spaces -= 2
            else:
                p = 1
                while p <= down_outer_spaces:
                    print(" ", end = "")
                    p += 1
                j = 1
                while j <= stars:
                    print("*", end = "")
                    j += 1
                stars += 2
                down_outer_spaces -= 1
            # print(print_pyramid(5))
                print()
print_pyramid(7)