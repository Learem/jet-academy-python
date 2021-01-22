def get_num(char):
    if "." in char:
        return float(char)
    else:
        return int(char)


def matrix_print(matrix, is_res=True):
    if matrix:
        if is_res:
            print("The result is:")
        for j in range(len(matrix)):
            print(" ".join([str(item) for item in matrix[j]]))
    print()


def matrix_input(num):
    msg = ""
    if num == 1:
        msg = "first "
    elif num == 2:
        msg = "second "
    if num == 3:
        n_a, m_a = [int(char) for char in input("Enter matrix size: ").split()]
    else:
        n_a, m_a = [int(char) for char in input("Enter size of " + msg + "matrix: ").split()]
    print("Enter " + msg + "matrix: ")
    matrix_a = []
    for i in range(n_a):
        matrix_a.append([get_num(char) for char in input().split()])
    return matrix_a


def matrix_addition(matrix_a, matrix_b):
    n_rows_a = len(matrix_a)
    n_cols_a = len(matrix_a[0])
    n_rows_b = len(matrix_b)
    n_cols_b = len(matrix_b[0])
    if n_rows_a != n_rows_b or n_cols_a != n_cols_b:
        print("The operation cannot be performed.")
        return []
    else:
        matrix_c = []
        for i in range(n_rows_a):
            matrix_c.append([matrix_a[i][k] + matrix_b[i][k] for k in range(n_cols_a)])
        return matrix_c


def matrix_dot_multiply(matrix_a, const):
    matrix_c = []
    for i in range(len(matrix_a)):
        matrix_c.append([round(matrix_a[i][k] * const, 2) for k in range(len(matrix_a))])
    return matrix_c


def matrix_dot_divide(matrix_a, const):
    matrix_c = []
    for i in range(len(matrix_a)):
        matrix_c.append([matrix_a[i][k] / const for k in range(len(matrix_a))])
    return matrix_c


def matrix_multiply(matrix_a, matrix_b):
    n_rows_a = len(matrix_a)
    n_cols_a = len(matrix_a[0])
    n_rows_b = len(matrix_b)
    n_cols_b = len(matrix_b[0])
    if n_cols_a != n_rows_b:
        print("The operation cannot be performed.")
        return []
    else:
        matrix_c = []
        for i in range(n_rows_a):
            matrix_c.append([])
            for j in range(n_cols_b):
                res = 0
                for k in range(n_cols_a):
                    res += matrix_a[i][k] * matrix_b[k][j]
                matrix_c[i].append(res)
        return matrix_c


def matrix_transpose(matrix_a, tip):
    matrix_c = []
    n_rows_a = len(matrix_a)
    n_cols_a = len(matrix_a[0])
    for i in range(n_cols_a):
        if tip == "main":
            matrix_c.append([matrix_a[k][i] for k in range(n_rows_a)])
        elif tip == "side":
            matrix_c.append([matrix_a[n_rows_a - k - 1][n_cols_a - i - 1] for k in range(n_rows_a)])
        else:
            break
    for i in range(n_rows_a):
        if tip == "vert":
            matrix_c.append([matrix_a[i][n_cols_a - k - 1] for k in range(n_cols_a)])
        elif tip == "hor":
            matrix_c.append([matrix_a[n_rows_a - i - 1][k] for k in range(n_cols_a)])
        else:
            break
    return matrix_c


def matrix_minor(matrix_a, n, m):
    matrix_c = []
    for j in range(len(matrix_a)):
        if n != j:
            matrix_c.append([matrix_a[j][k] for k in range(len(matrix_a[0])) if k != m])
    return matrix_c


def calc_det(matrix_a):
    n_rows_a = len(matrix_a)
    if n_rows_a == 1:
        return matrix_a[0][0]
    if n_rows_a == 2:
        return matrix_a[0][0] * matrix_a[1][1] - matrix_a[0][1] * matrix_a[1][0]
    if n_rows_a > 2:
        res = 0
        for i in range(n_rows_a):
            matrix_c = []
            for j in range(n_rows_a):
                if i != j:
                    matrix_c.append([matrix_a[j][k] for k in range(1, n_rows_a)])
            res += matrix_a[i][0] * (-1) ** i * calc_det(matrix_c)
        return res


def calculate_det(matrix_a):
    n_rows_a = len(matrix_a)
    n_cols_a = len(matrix_a[0])
    if n_rows_a != n_cols_a:
        print("The operation cannot be performed.")
        print()
    else:
        print("The result is:")
        print(calc_det(matrix_a))
        print()


def matrix_cofactor(matrix_a):
    matrix_c = []
    n_rows_a = len(matrix_a)
    n_cols_a = len(matrix_a[0])
    for i in range(n_rows_a):
        matrix_c.append([])
        for j in range(n_cols_a):
            matrix_c[i].append((-1) ** (i + j) * calc_det(matrix_minor(matrix_a, i, j)))
    return matrix_c


def matrix_inverse(matrix_a):
    n_rows_a = len(matrix_a)
    n_cols_a = len(matrix_a[0])
    if n_rows_a != n_cols_a:
        print("The operation cannot be performed.")
        print()
        return []
    else:
        det_a = calc_det(matrix_a)
        if det_a == 0:
            print("This matrix doesn't have an inverse.")
            print()
            return []
        else:
            return matrix_dot_divide(matrix_transpose(matrix_cofactor(matrix_a), "main"), det_a)


while True:
    print("1. Add matrices")
    print("2. Multiply matrix by a constant")
    print("3. Multiply matriсes")
    print("4. Transpose matrix")
    print("5. Calculate a determinant")
    print("6. Inverse matrix")
    print("0. Exit")
    my_choice = int(input("Your choice: "))
    if my_choice == 0:
        break
    if my_choice == 1:
        matrix_1 = matrix_input(1)
        matrix_2 = matrix_input(2)
        matrix_print(matrix_addition(matrix_1, matrix_2))
    if my_choice == 2:
        matrix_1 = matrix_input(0)
        matrix_print(matrix_dot_multiply(matrix_1, get_num(input("Enter constant: "))))
    if my_choice == 3:
        matrix_1 = matrix_input(1)
        matrix_2 = matrix_input(2)
        matrix_print(matrix_multiply(matrix_1, matrix_2))
    if my_choice == 4:
        print()
        print("1. Main diagonal")
        print("2. Side diagonal")
        print("3. Vertical line")
        print("4. Horizontal line")
        my_choice = int(input("Your choice: "))
        matrix_1 = matrix_input(3)
        if my_choice == 1:
            matrix_print(matrix_transpose(matrix_1, "main"))
        if my_choice == 2:
            matrix_print(matrix_transpose(matrix_1, "side"))
        if my_choice == 3:
            matrix_print(matrix_transpose(matrix_1, "vert"))
        if my_choice == 4:
            matrix_print(matrix_transpose(matrix_1, "hor"))
    if my_choice == 5:
        matrix_1 = matrix_input(3)
        calculate_det(matrix_1)
    if my_choice == 6:
        matrix_1 = matrix_input(3)
        matrix_print(matrix_inverse(matrix_1))
