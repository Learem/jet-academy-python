class TetrisPiece:
    def __init__(self, form, position, m_width, m_height):
        self.form = form
        self.position = position
        self.width = m_width
        self.height = m_height
        self.rotate_position = 0
        self.rotates = [[0, 0, 0, 0]]
        self.can_move = True

    def rotate(self):
        if self.can_move:
            rot_position = []
            new_position = (self.rotate_position + 1) % len(self.rotates)
            new_rotation = self.rotates[new_position]
            no_space = False
            for ii in range(len(self.position)):
                rot_position.append(self.position[ii] + new_rotation[ii])
                if (rot_position[ii] < 0) or (rot_position[ii] > (self.width * self.height - 1)):
                    no_space = True
            if not no_space:
                self.position = rot_position
                self.rotate_position = new_position

    def left(self):
        if self.can_move:
            new_position = list.copy(self.position)
            border = True
            for ii in range(len(self.position)):
                if self.position[ii] % self.width == 0:
                    border = False
                    break
                else:
                    new_position[ii] = new_position[ii] - 1
            if border:
                self.position = new_position

    def right(self):
        if self.can_move:
            new_position = list.copy(self.position)
            border = True
            for ii in range(len(self.position)):
                if self.position[ii] % self.width == self.width - 1:
                    border = False
                    break
                else:
                    new_position[ii] = new_position[ii] + 1
            if border:
                self.position = new_position

    def down(self):
        if self.can_move:
            new_position = []
            for num in self.position:
                new_position.append(num + 10)
            self.position = new_position

    def check_bottom(self, matrix):
        if self.can_move:
            m = len(matrix[0])
            n = len(matrix)
            bottom = []
            for num in self.position:
                if num + 10 not in self.position:
                    bottom.append(num)
            for num in bottom:
                ch_num = num + 10
                if ch_num > (m * n - 1):
                    self.can_move = False
                    for pos in self.position:
                        matrix[pos // m][pos % m] = '0'
                    break
                elif matrix[ch_num // m][ch_num % m] == '0':
                    self.can_move = False
                    for pos in self.position:
                        matrix[pos // m][pos % m] = '0'
                    break

    def check_end(self):
        if not self.can_move:
            for ii in range(self.width):
                if ii in self.position:
                    print('Game Over!')
                    return True
        return False


class PieceO(TetrisPiece):
    def __init__(self, position, m_width, m_height):
        super().__init__('O', position, m_width, m_height)
        self.rotates = [0, 0, 0, 0]

    def rotate(self):
        pass


class PieceI(TetrisPiece):
    def __init__(self, position, m_width, m_height):
        super().__init__('I', position, m_width, m_height)
        self.rotates = [1, 10, 19, 28], [-1, -10, -19, -28]


class PieceS(TetrisPiece):
    def __init__(self, position, m_width, m_height):
        super().__init__('S', position, m_width, m_height)
        self.rotates = [1, -10, -1, -12], [-1, 10, 1, 12]


class PieceZ(TetrisPiece):
    def __init__(self, position, m_width, m_height):
        super().__init__('Z', position, m_width, m_height)
        self.rotates = [[-1, -10, 1, -8], [1, 10, -1, 8]]


class PieceL(TetrisPiece):
    def __init__(self, position, m_width, m_height):
        super().__init__('L', position, m_width, m_height)
        self.rotates = [[-2, 9, 20, 11], [1, 1, -10, -12], [-1, -10, 1, 12], [2, 0, -11, -11]]


class PieceJ(TetrisPiece):
    def __init__(self, position, m_width, m_height):
        super().__init__('J', position, m_width, m_height)
        self.rotates = [[1, 1, 10, 8], [10, -10, -21, -21], [-10, -1, 10, 21], [-1, 10, 1, -8]]


class PieceT(TetrisPiece):
    def __init__(self, position, m_width, m_height):
        super().__init__('T', position, m_width, m_height)
        self.rotates = [[0, 9, 18, 0], [0, -1, -10, 0], [1, 2, 11, -1], [-1, -10, -19, 1]]


def init_board(m, n):
    return [["-" for _ in range(m)] for _ in range(n)]


def print_board(matrix, t_piece=None):
    for ii in range(len(matrix)):
        for jj in range(len(matrix[0])):
            if t_piece and (ii * len(matrix[0]) + jj in t_piece.position):
                print('0', end='')
            else:
                print(matrix[ii][jj], end='')
            if jj != len(matrix[0]) - 1:
                print(' ', end='')
        print()
    print()


def break_row(matrix):
    n = len(matrix)
    for ii in range(n):
        row = "".join(matrix[n - ii - 1])
        if row == '0' * len(matrix[0]):
            del matrix[n - ii - 1]
    for _ in range(n - len(matrix)):
        matrix.insert(0, list('-' * len(matrix[0])))


def set_piece(matrix, t_piece):
    m = len(matrix[0])
    n = len(matrix)
    no_space = False
    for num in t_piece.position:
        if matrix[num // m][num % m] == '0':
            no_space = True
    if no_space:
        return []
    else:
        new_board = [["0" if jj * m + ii in t_piece.position else matrix[jj][ii] for ii in range(m)] for jj in range(n)]
    # for num in t_piece.position:
    #     if num < m * n:
    #         matrix[num // m][num % m] = '0'
        return new_board


piece = None
board = []
res_board = []
width = 0
height = 0
mode = "start"
while mode != "exit":
    command = input()
    if command == "exit":
        mode = "exit"
        continue
    if mode == "start":
        values = command.split()
        width = int(values[0])
        height = int(values[1])
        board = init_board(width, height)
        print_board(board)
        mode = "piece"
        continue
    if mode == "piece" and command == "piece":
        command = input()
        if command in ["O", "I", "S", "Z", "L", "J", "T"]:
            if command == "I":
                piece = PieceI([4, 14, 24, 34], width, height)
            elif command == "O":
                piece = PieceO([4, 14, 15, 5], width, height)
            elif command == "S":
                piece = PieceS([5, 4, 14, 13], width, height)
            elif command == "Z":
                piece = PieceZ([4, 5, 15, 16], width, height)
            elif command == "L":
                piece = PieceL([4, 14, 24, 25], width, height)
            elif command == "J":
                piece = PieceJ([5, 15, 25, 24], width, height)
            elif command == "T":
                piece = PieceT([4, 14, 24, 15], width, height)
            print_board(board, piece)
            piece.check_bottom(board)
            continue
    if mode == "piece" and command == "break":
        break_row(board)
        print_board(board)
        continue
    if mode in ("move", "piece"):
        if command == "rotate":
            piece.rotate()
            piece.check_bottom(board)
            piece.down()
            piece.check_bottom(board)
            print_board(board, piece)
            if piece.check_end():
                mode = "exit"
                continue
        if command == "left":
            piece.left()
            piece.check_bottom(board)
            piece.down()
            piece.check_bottom(board)
            print_board(board, piece)
            if piece.check_end():
                mode = "exit"
                continue
        if command == "right":
            piece.right()
            piece.check_bottom(board)
            piece.down()
            piece.check_bottom(board)
            print_board(board, piece)
            if piece.check_end():
                mode = "exit"
                continue
        if command == "down":
            piece.down()
            piece.check_bottom(board)
            print_board(board, piece)
            if piece.check_end():
                mode = "exit"
                continue
        if not piece.can_move:
            mode = "piece"
