board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def solve(b):
    find = find_empty(b)

    if not find:
        return True
    else:
        x, y = find

    for i in range(1, 10):
        if is_valid(b, i, x, y):
            b[x][y] = i

            if solve(b):
                return True

            b[x][y] = 0


def is_valid(b, num, x, y):
    # check row
    for i in range(len(b[0])):
        if b[x][i] == num and y != i:
            return False

    # check column
    for i in range(len(b)):
        if b[i][y] == num and x != i:
            return False

    # check box
    box_x = y // 3
    box_y = x // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if b[i][j] == num and (i, j) != (x, y):
                return False

    return True


def print_board(b):
    for i in range(len(b)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(b[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(b[i][j])
            else:
                print(str(b[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return i, j
    return None


print_board(board)
solve(board)
print("__________________________")
print_board(board)
