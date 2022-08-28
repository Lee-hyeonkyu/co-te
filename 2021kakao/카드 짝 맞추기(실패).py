board = [[3, 0, 0, 2], [0, 0, 1, 0], [0, 1, 0, 0], [2, 0, 0, 3]]
r = 0
c = 1
# 틀린이유 : ex) 같은 카드가 0,0과 2,2에 있다고 한다면 최소거리가 3임. 43.3점


def search(board, r, c, point, cnt):
    board[r][c] = 0
    for i in range(4):
        for j in range(4):
            if point == board[i][j]:
                if (i == r) or (j == c):
                    cnt += 1
                else:
                    cnt += 2
                r = i
                c = j
                break
        if board[r][c] != 0:
            break
    board[r][c] = 0
    point = board[r][c]
    return board, cnt, point, r, c


def num_search(board, r, c, point, cnt):
    for i in range(4):
        if board[r][i] != point:
            cnt += 1
            c = i
            break
        elif board[i][c] != point:
            cnt += 1
            r = i
            break
    point = board[r][c]
    if point == 0:
        for i in range(4):
            if board[r][c] != 0:
                break
            for j in range(4):
                if board[i][j] != 0:
                    r = i
                    c = j
                    cnt += 2
                    break

    point = board[r][c]
    return cnt, point, r, c


def solution(board, r, c):
    point = board[r][c]
    cnt, maxx, answer = 0, 0, 0
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                maxx += 1
    answer = maxx
    maxx //= 2

    while maxx:
        if point != 0:
            board, cnt, point, r, c = search(board, r, c, point, cnt)

            maxx -= 1
        else:
            cnt, point, r, c = num_search(board, r, c, point, cnt)

    return answer + cnt


print(solution(board, r, c))
