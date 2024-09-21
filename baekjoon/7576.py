from collections import deque

m, n = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
day = 0

dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]

q = deque([i, j] for i in range(n) for j in range(m) if board[i][j] == 1)

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx < n and 0 <= ny < m and not board[nx][ny]:
            board[nx][ny] = board[x][y] + 1
            q.append([nx, ny])

for i in board:
    day = max(max(i), day)
    if i.count(0):
        day = 0
        break

print(day - 1)
