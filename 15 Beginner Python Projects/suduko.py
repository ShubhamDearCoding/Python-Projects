# import sys
# sys.setrecursionlimit(10000)  # Set the recursion limit to a higher value

def find_next_empty(puzzle):
    # finds the next row, col on the puzzle that's not filled yet --> rep with -1
    # return row, col tuple (or (None, None) if there is none)

    #keep in mind that we are using 0-8 for our indices
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
          
    return None, None #if no spaces in the puzzle are empty (-1)

def is_valid(puzzle, guess, row, col):
    # figures out whether the guess at the row/col of the puzzle is a valid guess 
    # returns True if is valid, False otherwise

    # let's start with the row:
    row_vals = puzzle[row]
    if guess in row_vals: 
        return False

    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    # and then the square 
    # this is tricky, but we want to get where the 3x3 square starts 
    # and iterate over the three values in the row/column 
 
    row_start = (row // 3) * 3 #1//  
    col_start = (col // 3) * 3    

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False 

    return True


def solve_sudoko(puzzle):
    # solve sudoku using backtracking!
    # our puzzle is a list of lists, where each inner list is a row in our sudoku puzzle 
    # return whether a solution exists
    # mutates puzzle to be the solution (if solution exists)

    # step 1: choose somewhere on the puzzle to make a guess 

    row, col = find_next_empty(puzzle)
    # step 1.1: if there's nowwhere left, them we're done because we only allowed valid inputs 
    if row is None:
        return True 

    # step 2: if there  is a place to put a number, then make a guess between 1 and 9
    for guess in range(1, 10): # range(1, 10) is 1,2,3, ... 9
         # step 3: check if this is a valid guess 
        if is_valid(puzzle, guess, row, col):
            # step 3.1: if this is valid, then place that guess on the puzzle!
            puzzle[row][col] = guess 
            # now recurse using the puzzle!
            # step 4: recursively call our function 
            if solve_sudoko(puzzle):
                    return True 

        # step 5: if not valid OR if our guess does not solve the puzzle, then we need to 
        # backtrack and try a new number 
        puzzle[row][col] = -1 # reset the guess 

    # step 6: if none  of the numbers that we try work, then this puzzle is UNSOLVABLE!!
    
    return False 

def print_puzzle(puzzle):
    for row in puzzle:
        print(row)

if __name__ == '__main__':
    example_board = [
    [5, 3, -1, -1, 7, -1, -1, -1, -1],
    [6, -1, -1, 1, 9, 5, -1, -1, -1],
    [-1, 9, 8, -1, -1, -1, -1, 6, -1],
    [8, -1, -1, -1, 6, -1, -1, -1, 3],
    [4, -1, -1, 8, -1, 3, -1, -1, 1],
    [7, -1, -1, -1, 2, -1, -1, -1, 6],
    [-1, 6, -1, -1, -1, -1, 2, 8, -1],
    [-1, -1, -1, 4, 1, 9, -1, -1, 5],
    [-1, -1, -1, -1, 8, -1, -1, 7, 9]
]

    solve_sudoko(example_board)
    print_puzzle(example_board)
    print("Sudoku solved!")

    # print(solve_sudoko(example_board))
    # print(example_board)

# def fun(a, b):
#     if a == b:
#         return False

# if fun(2, 2):
#     print('Match')

# print(fun(1, 2))

# if fun(1, 2):
#     print('no match')

# if None:
#     print('yes')
# else:
#     print('No')
#output: No
# None is identical to False

 def fun(a, b):
    if a == b:
        return False
    else
        fun(a, b)

def fun(x):
    if x == 0:
        print('x is 0 here -top')
        return False
        print('x is 0 here -bottom')
    else:
        fun(x-1)
    print(x)
    
x = fun(5)
print(x)
# x is 0 here -top
# 1
# 2
# 3
# 4
# 5
# None

y = fun(0)
print(y)
# False

