from collections import deque
import copy

n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]


wall = []

dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]


def bfs(space):
    q = deque()

    for i in range(n):
        for j in range(m):
            if board[i][j] == 2:
                q.append([i, j])
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not space[nx][ny]:
                space[nx][ny] = 2
                q.append([nx, ny])

    tmp = 0
    for i in range(n):
        for j in range(m):
            if not space[i][j]:
                tmp += 1
    return tmp


def solution():
    safe_zone = 0

    def bt(wall):
        nonlocal safe_zone
        if len(wall) == 3:
            space = copy.deepcopy(board)
            for d, w in wall:
                space[d][w] = 1
            safe_zone = max(bfs(space), safe_zone)
            return
        for i in range(n):
            for j in range(m):
                if not board[i][j] and [i, j] not in wall:
                    if not len(wall) or (len(wall) >= 1 and wall[-1] < [i, j]):
                        wall.append([i, j])
                        bt(wall)
                        wall.pop()

    bt([])
    return safe_zone


print(solution())
