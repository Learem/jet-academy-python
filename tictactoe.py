def grid_print(grid):
    grid = grid.replace("_", " ")
    print("---------")
    print("|", grid[0], grid[1], grid[2], "|")
    print("|", grid[3], grid[4], grid[5], "|")
    print("|", grid[6], grid[7], grid[8], "|")
    print("---------")


def grid_split(grid):
    grid_list = []
    for i in range(3):
        grid_list.append(grid[i*3: i*3+3])
        grid_list.append(grid[i] + grid[i+3] + grid[i+6])
        if i != 1:
            grid_list.append(grid[i] + grid[4] + grid[8-i])
    return grid_list


def analyze_state(grid):
    count_x = grid.count("X")
    count_o = grid.count("O")
    count_empty = grid.count("_")
    cells_list = grid_split(grid)
    if (abs(count_x - count_o) > 1) or ("XXX" in cells_list and "OOO" in cells_list):
        return "Impossible"
    elif "XXX" in cells_list:
        return "X wins"
    elif "OOO" in cells_list:
        return "O wins"
    elif count_empty == 0:
        return "Draw"
    else:
        return "Game not finished"


def check_busy(grid, r, c):
    cell = (r - 1) * 3 + c - 1
    return grid[cell] in "OX"


cells = "_________"
grid_print(cells)
turn = "X"
while True:
    try:
        row, col = [int(char) for char in input("Enter the coordinates: ").split()]
    except ValueError:
        print("You should enter numbers!")
        continue
    if (row > 3) or (col > 3) or (row < 1) or (col < 1):
        print("Coordinates should be from 1 to 3!")
        continue
    elif check_busy(cells, row, col):
        print("This cell is occupied! Choose another one!")
        continue
    else:
        coord = (row - 1) * 3 + col - 1
        cells = cells[:coord] + turn + cells[coord+1:]
        grid_print(cells)
        state = analyze_state(cells)
        if state in ["X wins", "O wins", "Draw"]:
            print(state)
            break
        elif turn == "X":
            turn = "O"
        elif turn == "O":
            turn = "X"
