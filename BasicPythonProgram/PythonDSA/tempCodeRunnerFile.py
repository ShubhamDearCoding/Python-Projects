def print_pyramid(rows):
    stars = 1
    spaces = 5
    for i in range(rows):
        p = 1
        while p <= stars:
            print("*", end = "")
            p += 1
        j = 1
        while j <= spaces:
            print(" ", end = "")
            j += 1
        k = 1
        while k <= stars:
            print("*", end = "")
            k += 1
        if i < 2//2:
            stars += 0
            spaces -= 0
        else:
            stars += 1
            spaces -= 2
        # print(print_pyramid(5))
        print()
print_pyramid(5)