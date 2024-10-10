import sys

sudoku = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]


# blank = []
# for i in range(1, 10):
#     for line in sudoku:
#         if i not in line:
#             blank.append(i)


def cube_check(n, m):
    check = [0] * 10
    for i in range(n - 3, n):
        for num in sudoku[i][m - 3 : m]:
            check[num] += 1

    if check[0] == 1:
        return check.index(0)

    return 0


def line_check():

    pass
