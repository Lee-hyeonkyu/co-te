from collections import deque

n = int(input())

sea = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
shk = []
time = 0

for i in range(n):
    for j in range(n):
        if sea[i][j] == 9:
            shk.append(i)
            shk.append(j)


def bfs(x, y):
    visited = [[0]*n for _ in range(n)]
    q = deque([[x, y]])
    feed = []
    visited[x][y] = 1

    while q:
        i, j = q.popleft()

        for idx in range(4):
            m_i, m_j = dx[idx]+i, dy[idx]+j

            if m_i >= 0 and m_i < n and m_j >= 0 and m_j < n and not visited[m_i][m_j]:
                if sea[x][y] > sea[m_i][m_j] and sea[m_i][m_j]:
                    visited[m_i][m_j] = visited[i][j] + 1
                    feed.append((visited[m_i][m_j]-1, m_i, m_j))
                elif sea[x][y] == sea[m_i][m_j]:
                    visited[m_i][m_j] = visited[i][j] + 1
                    q.append([m_i, m_j])
                elif sea[m_i][m_j] == 0:
                    visited[m_i][m_j] = visited[i][j] + 1
                    q.append([m_i, m_j])

    return sorted(feed, key=lambda x: (x[0], x[1], x[2]))


i, j = shk
size = [2, 0]

while 1:
    sea[i][j] = size[0]
    feed = deque(bfs(i, j))

    if not feed:
        break

    step, x_i, y_i = feed.popleft()
    time += step
    size[1] += 1

    if size[0] == size[1]:
        size[0] += 1
        size[1] = 0

    sea[i][j] = 0
    i, j = x_i, y_i

print(time)
