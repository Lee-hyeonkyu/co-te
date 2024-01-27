n = int(input())
pos = ((0, 1), (1, 0), (0, -1), (-1, 0))
board = [[0] * n for _ in range(n)]
score = {}

first = 1


def cond_2(lst: list) -> list:
    space = []
    mx = 0
    for index in lst:
        x, y = index
        tmp = 0
        for p in range(4):
            nx = x + pos[p][0]
            ny = y + pos[p][1]
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] == 0:
                    tmp += 1
        mx = max(tmp, mx)
        space.append(tmp)
        # cond_3
    return lst[space.index(mx)]


def cond_1(num: int) -> list:
    # 위치 리스트 출력
    check = [[0] * n for _ in range(n)]
    mx = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                tmp = 0
                for p in range(4):
                    nx = pos[p][0] + i
                    ny = pos[p][1] + j
                    if 0 <= nx < n and 0 <= ny < n and board[nx][ny] in score[num]:
                        tmp += 1
                mx = max(tmp, mx)
                check[i][j] = tmp

    lst = []
    if mx:
        for i in range(n):
            for j in range(n):
                if check[i][j] == mx:
                    lst.append([i, j])

        if len(lst) < 2:
            return lst[0]
        else:
            return cond_2(lst)

    else:
        lst = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 0:
                    lst.append([i, j])
        return cond_2(lst)


for _ in range(n**2):
    x = list(map(int, input().split()))
    score[x[0]] = x[1:]
    if first:
        board[1][1] = x[0]
        first = 0
    else:
        r, c = cond_1(x[0])
        board[r][c] = x[0]

# 위까지 보드 완성
answer = 0


for i in range(n):
    for j in range(n):
        tmp = 0
        for p in range(4):
            nx = i + pos[p][0]
            ny = j + pos[p][1]
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] in score[board[i][j]]:
                    tmp += 1
        if tmp == 1:
            answer += 1
        elif tmp == 2:
            answer += 10
        elif tmp == 3:
            answer += 100
        elif tmp == 4:
            answer += 1000
print(answer)
