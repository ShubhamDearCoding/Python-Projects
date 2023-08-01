import random
class Board:
    def _init_(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        self.board = self.make_new_board()
        self.assign_values_to_board()

        self.dug =set()

    def make_new_board(self): 

        def assign_values_to_board(self):
            for r in range(self.dim_size):
                for c in range(self.dim_size):
                    if self.board[r][c] == '*':
                        continue 
                    self.board[r][c] = self.get_num_neighboring_bombs(r, c)

    def   get_num_neighbouring_bombs(self, row, col):
            num_neighbouring_bombs = 0
            for r in range(row-1, (row+1)+1):
                for c in range(col-1, (col+1)+1):
                    if r == row and c == col:
                        continue
                    if self.board[r][c] == '*':
                        num_neighouring_bombs += 1

    def   dig(self, row, col):
            self.dug.add((row, col))

            if self.board[row][col] == '*':
                return False 
            elif self.board[row][col] > 0:
                return True 
            for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
                for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                    if (r, c) in self.dug:
                        continue
                    self.dig(r,c)
            return True 

    def _str_(self):

        visible_board =  [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row,col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = '  ' 

            string_rep = '  '
            
            widths = []
            for idx in range(self.dim_size):
                columns = map( lambda x: x[idx], visible_board)
                widths.append(
                    len(
                        max(column, key = len)
                    )
                )

                     
            
        

def play(dim_size=10, num_bombs=10):
    board = Board(dim_size, num_bombs)




    

    board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]

    bombs_planted = 0
    while bombs_planted < self.num_bombs:
        loc = random.randit(0, self.dim_size**2 -1)             
        row = loc // self.dim_size
        col = loc % self.dim_size   

        if board[row][col] == '*':
            continue
        board[row][col] = '*'
        bombes_planted += 1

    return board

    (dim_size:=10, num_bombs:=10)

def play(dim_size=10, num_bombs=10):
      board = Board(dim_size, num_bombs)

      while len(board.dug) < board.dim_size ** 2 - num_bombs:
            print(board)
            user_input = re.split (input("Where would you like to dig?" Input as row,col: ''))
            row, col = int(user_input[0])
            if row < 0 or row >= board.dim_size or col < 0 or col >= dim_size:
                print("Invalid location. Try again.")
                continue

            safe = board.dig(row, col)
            if not safe:

                break 

            if safe:
                print("CONGRATULATIONS!!!! YOU ARE VICTORIOUS!")
            else:
                print("SORRY GAME OVER :(")
                board.dug = [(r,c) for r in range(board.dim_size) for c in range(board.dim_size)]
                print(board)

    if _name_ == '_main_':
        play()




    