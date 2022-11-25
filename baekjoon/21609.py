from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 접근법: 해당 블럭을 돌면서 블럭의 길이가 2보다 크고 0과 개수가 가장 많은 블럭의 크기를 찾기.


def bfs(x, y, p):
    q = deque()
    q.append(x, y)

    for _ in range(m):
        visited = [[[0, 0]] * n for _ in range(n)]
        # [크기,0의 개수]
        while q:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

            if nx < 0 or ny < 0 or n <= nx or n <= ny:
                continue
            if board[nx][ny] == p and visited[nx][ny] == [0, 0]:
                q.append(nx, ny)
                visited[nx][ny][0] += 1
            elif board[nx][ny] == 0 and visited[nx][ny] == [0, 0]:
                q.append(nx, ny)
                visited[nx][ny][0] += 1
                visited[nx][ny][1] += 1
