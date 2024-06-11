def is_valid(board,row,col,num):
    for i in range(9):
        if board[row][i]==num:
            return False
        
    for i in range(9):
        if board[i][col] == num:
            return False
    start_row,start_col = 3 * (row//3), 3*(col//3)
    for i in range(start_row, start_row+3):
        for j in range(start_col,start_col+3):
            if board[i][j] == num:
                return False
    return True


def solve_sudoku(board):
    empty_cell = find_empty_location(board)
    if not empty_cell:
        return True
    row,col = empty_cell

    for num in range(1,10):
        if is_valid(board,row,col,num):
            board[row][col] = num

            if solve_sudoku(board):
                return True
            board[row][col] = 0

    return False
def find_empty_location(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i,j)
    return None
def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else "," for num in row))
sudoku_board = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]


if solve_sudoku(sudoku_board):
    print("sudoku puzzle solved successfully")
    print_board(sudoku_board)
else:
    print("No solution exist for this problem")
    






