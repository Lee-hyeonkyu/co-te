from collections import deque

dx = (1, 0, 0, -1)
dy = (0, 1, -1, 0)

for _ in range(int(input())):
    m, n, k = map(int, input().split())
    board = [[0] * m for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    q = deque()
    for i in range(k):
        y, x = map(int, input().split())
        board[x][y] = 1
    cnt = 0

    for i in range(n):
        for j in range(m):
            if board[i][j] and not visited[i][j]:
                cnt += 1
                visited[i][j] = 1
                q.append([i, j])

                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if (
                            0 <= nx < n
                            and 0 <= ny < m
                            and board[nx][ny]
                            and not visited[nx][ny]
                        ):
                            visited[nx][ny] = 1
                            q.append([nx, ny])
    print(cnt)
