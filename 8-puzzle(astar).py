from collections import deque
import copy
import time

start = time.time()
puzzle = [[7, 2, 4], [5, 0, 6], [8, 3, 1]]  # [[3, 1, 2], [4, 5, 8], [0, 6, 7]]
answer = []
solve = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

q = deque()
# 하 상 좌 우
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# f, g, h, 부모노드
op_lst, cl_lst = [], []
# F-score: 총합
# H-score: 틀린 개수
# G-score: 시작-> 현재 node


def check_heuristic(ch_puzzle, solve):
    h_score = 0
    for i in range(3):
        for j in range(3):
            if ch_puzzle[i][j] != solve[i][j]:
                h_score += 1
    return h_score


for i in range(3):
    for j in range(3):
        if not puzzle[i][j]:
            q.append([i, j])

g_score = 1

while q:
    x, y = q.popleft()
    if puzzle == solve:
        answer = puzzle
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < 3 and 0 <= ny < 3:
            tmp_puz = copy.deepcopy(puzzle)
            tmp_puz[x][y], tmp_puz[nx][ny] = tmp_puz[nx][ny], tmp_puz[x][y]
            h_score = check_heuristic(tmp_puz, solve)
            op_lst.append(
                [g_score + h_score, g_score, h_score, tmp_puz[x][y], tmp_puz, [nx, ny]]
            )
    op_lst.sort(key=lambda x: x[0])
    cl_lst.append(op_lst.pop(0))
    puzzle = cl_lst[-1][-2]
    q.append(cl_lst[-1][-1])
    g_score += 1

print(answer)
end = time.time()

print(end - start)
