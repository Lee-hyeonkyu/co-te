pos = ((0, 1), (1, 0), (0, -1), (-1, 0))
r, c, n = map(int, input().split())

board = [list(input()) for _ in range(r)]
board_1 = [["O"] * c for _ in range(r)]
board_2 = [["O"] * c for _ in range(r)]


def bomb(space, space_1):
    for i in range(r):
        for j in range(c):
            if space[i][j] == "O":
                space_1[i][j] = "."
                for p in range(4):
                    nx = pos[p][0] + i
                    ny = pos[p][1] + j
                    if 0 <= nx < r and 0 <= ny < c:
                        space_1[nx][ny] = "."
    return space_1


if n == 1:
    for b in board:
        print("".join(b))
elif not n % 2:
    for i in range(r):
        print("O" * c)
else:
    board_1 = bomb(board, board_1)
    board_2 = bomb(board_1, board_2)

    if n % 4 == 3:
        for b in board_1:
            print("".join(b))
    else:
        for b in board_2:
            print("".join(b))
