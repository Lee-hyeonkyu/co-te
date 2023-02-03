n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

limit_x = n - 8
limit_y = m - 8
answer = 2500


def check(x, y):
    cnt = 0
    type = ["W", 'B']
    result1, result2 = 0, 0
    for i in range(x, x + 8):
        cnt += 1
        for j in range(y, y + 8):
            if board[i][j] == type[cnt % 2]:
                result1 += 1
            else:
                result2 += 1
            cnt += 1
    return min(result1, result2)


for i in range(limit_x+1):
    for j in range(limit_y+1):
        answer = min(check(i, j), answer)

print(answer)
