
grid = [[0, 0, 5, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 7, 0, 0, 0, 8, 0],
        [6, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 1, 0, 3, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 5, 0, 0, 9, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 2],
        [0, 0, 0, 4, 0, 0, 7, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 1],
        [0, 5, 0, 0, 0, 2, 0, 0, 0]
        ]
#You need to store the value in a variable, you just need to use 
        #it in checking the column.
#I need to check if a specific number in a specific position is not repeating.

def check_validity(row, column, num):
    global grid
    for i in range(0, 9):
        if grid[row][i] == num:
            return False
    for j in range(0, 9):
        if grid[j][column] == num:
            return False
    x = (row//3)*3
    y = (column//3)*3
    for m in range(0, 3):
        for n in range(0, 3):
            if grid[x+m][y+n] == num:
                return False
    return True
            
def solve():
    global grid
    for row in range(0, 9):
        for column in range(0, 9):
            if grid[row][column] == 0:
                for num in range(1, 10):
                    if check_validity(row, column, num):
                        grid[row][column] = num
                        if solve():
                            return True
                        grid[row][column] = 0
                return False 
    return True

if solve():
    for row in grid:
        print(row)
else:
    print("Has no solution")
