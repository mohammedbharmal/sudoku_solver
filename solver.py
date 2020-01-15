# Problem to be solved, Solution is given in the image separately to verify
game = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]


# Function to check if the number is present in the grid or not
# This function is a wrapper function with parameters to calculate the grid of the current position
def grid_call(p, j, k):
    if j < 3:
        return grid_check(p, 0, k)
    elif j >= 3 and j < 6:
        return grid_check(p, 3, k)
    else:
        return grid_check(p, 6, k)


# Function to check if the number is present in the grid or not
def grid_check(i, j, k):
    for l in range(i, i+3):
        for m in range(j, j+3):
            if game[l][m] == k:
                return False
    return True


# Function to check if the number is present in the row
def row_check(g, k):
    if k not in g:
        return True
    return False


# Function to check if the number is present in the column
def col_check(j, k):
    for l in range(9):
        if game[l][j] == k:
            return False
    return True


# Wrapper function the calls other functions to check if the number is valid for the current position
# Return true if number is valid, false otherwise
def check_all(g, i, j, k):
    # Calls function to check for row
    row = row_check(g, k)
    # Calls function to check for column
    col = col_check(j, k)
    grid = False
    if i < 3:
        grid = grid_call(0, j, k)
    elif i >= 3 and i < 6:
        grid = grid_call(3, j, k)
    else:
        grid = grid_call(6, j, k)
    return row and col and grid


# Main function to traverse the grid
def sudoku(game):
    for i, g in enumerate(game):
        for j, h in enumerate(g):
            # Check if number has already been assigned
            if h == 0:
                for k in range(1, 10):
                    if check_all(g, i, j, k):
                        game[i][j] = k
                        # Recursively call the method to check the grid is valid
                        if sudoku(game):
                            return True
                        # If number is not valid assign 0
                        game[i][j] = 0
                return False
    return True


for s, t in enumerate(game):
    print(t)
print()
if sudoku(game):
    for s, t in enumerate(game):
        print(t)
else:
    print("Invalid sudoku problem")
