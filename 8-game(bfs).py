from collections import deque
import copy
import time

start = time.time()
puzzle = [[7, 2, 4], [5, 0, 6], [8, 3, 1]]
answer = []
solve = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
history_pos = 9
# 하 우 상 좌 (0,1,2,3)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

q = deque()

for i in range(len(puzzle)):
    for j in range(len(puzzle)):
        if not puzzle[i][j]:
            q.append([i, j, puzzle, history_pos])

# 이전 위치값과 변경된 퍼즐과 현재 0의 위치를 가져가자.

while q:
    x, y, p, h = q.popleft()
    if p == solve:
        answer = p
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        puz = copy.deepcopy(p)
        if i != h and 0 <= nx < len(puz) and 0 <= ny < len(puz):
            # 스위칭
            puz[x][y], puz[nx][ny] = puz[nx][ny], puz[x][y]
            q.append([nx, ny, puz, (i - 2) % 4])

print(answer)
end = time.time()
print(end - start)
## 272초
