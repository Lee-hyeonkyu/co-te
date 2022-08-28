board = [[3, 0, 0, 2], [0, 0, 1, 0], [0, 1, 0, 0], [2, 0, 0, 3]]
r = 0
c = 1
# 46.7점
# 특수 케이스라도 만약 차이 2의 지점에 아직 지워지지 않은 카드가 있다면 ctrl + 방향키로  3칸을가야할 위치도 2번만에 갈 수 있음
# 또 사이에 카드가 많이 놓여있다면 ctrl + 방향키를 사용하지 못함.


def search(board, r, c, point, cnt, special):
    board[r][c] = 0
    if [r, c] in special:
        for i in range(4):
            for j in range(4):
                if point == board[i][j]:
                    if (abs(r-i) == 2) and (abs(c-j) == 2):
                        cnt += 3
                    elif (i == r) or (j == c):
                        cnt += 1
                    else:
                        cnt += 2
                    r = i
                    c = j
                    break
            if board[r][c] != 0:
                break
    else:
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
    if board[r][c] == 0:
        return board, cnt, point, r, c
    board[r][c] = 0
    point = board[r][c]
    return board, cnt, point, r, c


def num_search(board, r, c, point, cnt, special):
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
            for j in range(4):
                if board[i][j] != 0:
                    if [r, c] in special:
                        if (abs(r-i) == 2) and (abs(c-j) == 2):
                            cnt += 3
                        else:
                            cnt += 2
                    r = i
                    c = j
                    break
            if board[r][c] != 0:
                break

    point = board[r][c]
    return cnt, point, r, c


def solution(board, r, c):
    special = [[0, 0], [3, 0], [0, 3], [3, 3]]
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
            board, cnt, point, r, c = search(board, r, c, point, cnt, special)
            maxx -= 1
        else:
            cnt, point, r, c = num_search(board, r, c, point, cnt, special)
    return answer + cnt


print(solution(board, r, c))
