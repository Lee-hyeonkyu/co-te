from math import inf
from collections import deque


rectangle = [[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]]
characterX = 1
characterY = 3
itemX = 7
itemY = 8


def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()
    q.append([characterX*2, characterY*2])
    visited = [[1] * 150 for i in range(150)]
    space = [[inf] * 150 for i in range(150)]
    for i in rectangle:
        x1, y1, x2, y2 = map(lambda x: x*2, i)
        for j in range(x1, x2+1):
            for k in range(y1, y2+1):
                if x1 < j < x2 and y1 < k < y2:
                    space[j][k] = 0
                elif space[j][k]:
                    space[j][k] = 1

    while q:
        x, y = q.popleft()
        if x == itemX * 2 and y == itemY * 2:
            answer = visited[x][y] // 2
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if space[nx][ny] == 1 and visited[nx][ny] == 1:
                q.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1

    return answer


print(solution(rectangle, characterX, characterY, itemX, itemY))
