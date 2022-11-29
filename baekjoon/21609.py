from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 접근법: 해당 블럭을 돌면서 블럭의 길이가 2보다 크고 0과 개수가 가장 많은 블럭의 크기를 찾기.


def bfs(i, j, visited):
    q = deque()
    q.append([i, j])
    visited[i][j][0] = 0
    num = board[i][j]
    rainbow = []
    block_pos = []
    m = []
    while q:
        x, y = q.popleft()

        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]

            if 0 <= nx < n and 0 <= ny < n:
                print(nx, ny)
                print("hi")
                if board[nx][ny] == num and visited[nx][ny] == [0, 0]:
                    print('ssddddsssds')
                    q.append([nx, ny])
                    block_pos.append([nx, ny])
                    visited[nx][ny][0] += 1  # 블럭 + 1
                elif board[nx][ny] == 0 and visited[nx][ny] == [0, 0]:
                    print('h21')
                    q.append([nx, ny])
                    visited[nx][ny][0] += 1
                    visited[nx][ny][1] += 1  # 레인보우 + 1
                    rainbow.append([nx, ny])

    print(rainbow)
    print('------')
    print(block_pos)

    if rainbow[-1] >= block_pos[-1]:
        m.append(rainbow[-1])
    else:
        m.append(block_pos[-1])

    for i, j in rainbow:
        visited[i][j] = [0, 0]

    return [*m, block_pos + rainbow]


def check(board):
    visited = [[[0, 0]] * n for _ in range(n)]
    out = []

    for i in range(n):
        for j in range(n):
            if board[i][j] > 0 and not visited[i][j][0]:
                check_blk = bfs(i, j, visited)
                if check_blk[0] >= 2:
                    out.append(check_blk)

    out = sorted(out, key=lambda x: (
        x[0], x[1], x[2][0][0], x[2][0][1]), reverse=True)

    return out


def blockout(out):
    for i, j in out:
        board[i][j] = -2


def gravity(board):
    for i in range(n-1, -1, -1):
        for j in range(n):
            if board[i][j] >= 0:
                g = i
                while 1:
                    if 0 <= g+1 < n:
                        if board[g+i][j] == -2:
                            board[g+1][j] = board[g][j]
                            board[g][j] = -2
                            g += 1
                        else:
                            break
                    else:
                        break


def rotation(board):
    new_board = list(map(list, zip(*board)))[::-1]

    return new_board


score = 0

while True:
    block = check(board)
    if not block:
        break

    blockout(block[0][2], board)
    score += block[0][0] ** 2

    gravity(board)
    board = rotation(board)
    gravity(board)

print(score)
