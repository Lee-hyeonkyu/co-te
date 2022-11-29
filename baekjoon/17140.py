from collections import Counter

r, c, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(3)]
cnt = 0
check = 0


def arith(board, max_len, new_board):
    for i in board:
        temp = []
        counting_board = sorted(list(Counter(i).items()),
                                key=lambda x: ([x[1], x[0]]))
        for n, c in counting_board:
            if not n:
                continue
            temp.append(n)
            temp.append(c)
        max_len = max(max_len, len(temp))
        new_board.append(temp)

    for i in new_board:
        if len(i) < max_len:
            for _ in range(max_len - len(i)):
                i.append(0)


while cnt <= 100:
    if r <= len(board) and c <= len(board[0]) and board[r-1][c-1] == k:
        check = 1
        print(cnt)
        break
    max_len = 0
    new_board = []
    cnt += 1

    if len(board) >= len(board[0]):
        arith(board, max_len, new_board)
        board = new_board
    elif len(board) < len(board[0]):
        board = list(map(list, zip(*board)))
        arith(board, max_len, new_board)
        board = list(map(list, zip(*new_board)))

if not check:
    print(-1)
