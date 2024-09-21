from collections import deque

n, m = map(int, input().split())

board = [list(int(i) for i in input()) for _ in range(n)]


dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]

q = deque()
q.append([0, 0])

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 1:
            board[nx][ny] += board[x][y]
            q.append([nx, ny])

print(board[n - 1][m - 1])
