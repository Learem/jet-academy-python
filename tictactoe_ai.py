import random


def what_turn(board):
    if board.count("X") == board.count("O"):
        return "X"
    elif board.count("X") == board.count("O") + 1:
        return "O"
    else:
        return "Error"


def next_turn(char):
    return "O" if char == "X" else "X"


def game_print(board):
    print("---------")
    for i in range(3):
        print("|", end=" ")
        for k in range(3):
            char = board[i * 3 + k]
            if char == "_":
                char = " "
            print(char, end=" ")
        print("|")
    print("---------")


def game_state(board):
    lines = []
    for i in range(3):
        row = board[i * 3] + board[i * 3 + 1] + board[i * 3 + 2]
        lines.append(row)
        col = board[i] + board[i + 3] + board[i + 6]
        lines.append(col)
    diag = board[0] + board[4] + board[8]
    lines.append(diag)
    diag = board[2] + board[4] + board[6]
    lines.append(diag)
    if "XXX" in lines:
        return "X wins"
    elif "OOO" in lines:
        return "O wins"
    elif "_" not in board:
        return "Draw"
    else:
        return "Game not finished"


def check_busy(board, r, c):
    return "_" != board[(r - 1) * 3 + c - 1]


def make_turn(board, char, r, c):
    index = (r - 1) * 3 + c - 1
    return board[:index] + char + board[index + 1:]


def random_move(board):
    step = random.randint(1, board.count("_"))
    mod_string = board.replace("_", "*", step - 1)
    step = mod_string.index("_")
    row = step // 3 + 1
    col = step % 3 + 1
    return row, col


def medium_move(board, t):
    for i in range(len(board)):
        if board[i] == "_":
            if game_state(board[:i] + t + board[i + 1:]) == t + " wins":
                row = i // 3 + 1
                col = i % 3 + 1
                return row, col
    at = next_turn(t)
    for i in range(len(board)):
        if board[i] == "_":
            if game_state(board[:i] + at + board[i + 1:]) == at + " wins":
                row = i // 3 + 1
                col = i % 3 + 1
                return row, col
    return random_move(board)


def calc_rate(board, t, ind, maxi):
    row = ind // 3 + 1
    col = ind % 3 + 1
    next_game = make_turn(board, t, row, col)
    pr_stat = game_state(next_game)
    if pr_stat == t + " wins":
        if maxi:
            return 20
        else:
            return -20
    elif pr_stat == next_turn(t) + " wins":
        if maxi:
            return -20
        else:
            return 20
    elif pr_stat == "Draw":
        return 0
    else:
        t = next_turn(t)
        if maxi:
            rate = 100
            for i in range(len(next_game)):
                if next_game[i] == "_":
                    tmp = calc_rate(next_game, t, i, not maxi)
                    if tmp < rate:
                        rate = tmp
            return rate + 1
        else:
            rate = -100
            for i in range(len(next_game)):
                if next_game[i] == "_":
                    tmp = calc_rate(next_game, t, i, not maxi)
                    if tmp > rate:
                        rate = tmp
            return rate - 1


def hard_move(board, t):
    rate = -100
    step = -1
    for i in range(len(board)):
        if board[i] == "_":
            tmp = calc_rate(board, t, i, True)
            if tmp > rate:
                rate = tmp
                step = i
    row = step // 3 + 1
    col = step % 3 + 1
    return row, col


# the_game = input("Enter the cells: ")
random.seed()

while True:
    command = input("Input command: ")
    params = command.split()
    if len(params) > 0 and params[0] == "exit":
        break
    if len(params) != 3:
        print("Bad parameters!")
        continue
    if params[0] == "start":
        if params[1] not in ["user", "easy", "medium", "hard"]:
            print("Bad parameters!")
            continue
        if params[2] not in ["user", "easy", "medium", "hard"]:
            print("Bad parameters!")
            continue
        the_game = "_" * 9
        game_print(the_game)
        turn = "X"
        while True:
            diff = "user"
            if turn == "X" and params[1] in ["easy", "medium", "hard"]:
                diff = params[1]
            elif turn == "O" and params[2] in ["easy", "medium", "hard"]:
                diff = params[2]
            if diff != "user":
                print('Making move level "' + diff + '"')
                if diff == "medium":
                    x, y = medium_move(the_game, turn)
                elif diff == "hard":
                    x, y = hard_move(the_game, turn)
                else:
                    x, y = random_move(the_game)
                the_game = make_turn(the_game, turn, x, y)
                turn = next_turn(turn)
                game_print(the_game)
                stat = game_state(the_game)
                if stat in ["X wins", "O wins", "Draw"]:
                    print(stat)
                    break
            else:
                try:
                    x, y = [int(coord) for coord in input("Enter the coordinates: ").split()]
                except ValueError:
                    if the_game == "exit":
                        break
                    print("You should enter numbers!")
                    continue
                if x < 1 or x > 3 or y < 1 or y > 3:
                    print("Coordinates should be from 1 to 3!")
                    continue
                if check_busy(the_game, x, y):
                    print("This cell is occupied! Choose another one!")
                    continue
                else:
                    the_game = make_turn(the_game, turn, x, y)
                    turn = next_turn(turn)
                    game_print(the_game)
                    stat = game_state(the_game)
                    if stat in ["X wins", "O wins", "Draw"]:
                        print(stat)
                        break
    else:
        print("Bad parameters!")
        continue
