from collections import deque

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def check(x, y, tmp):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if not arr[nx][ny]:
                tmp.append([x, y])
                break


def bfs(x, y, visited):
    visited[x][y] = 1
    q = deque()
    q.append([x, y])

    while q:
        x, y = q.popleft()
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and arr[nx][ny]:
                visited[nx][ny] = 1
                q.append([nx, ny])


def count_island():
    cnt = 0
    visited = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if arr[i][j] and not visited[i][j]:
                cnt += 1
                bfs(i, j, visited)
    return cnt


def solution(n, m, arr):
    day = 0
    answer = 0
    while 1:
        tmp = []
        for i in range(n):
            for j in range(m):
                if arr[i][j] == 1:
                    check(i, j, tmp)
        print('-------', tmp)
        for x, y in tmp:
            arr[x][y] = 0
        day += 1
        cnt = count_island()
        if cnt >= 2:
            answer = day
            return answer
        elif not cnt:
            answer = -1
            return answer


print(solution(n, m, arr))
