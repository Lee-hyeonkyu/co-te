# 시간초과

import numpy as np

n = 2
m = 2
x = 0
y = 0
# move_lst = []
queries = [[2, 1], [0, 1], [1, 1], [0, 1], [2, 1]]


# def search(board, i, j, n, m):
#     for dx, dy in move_lst:
#         if 0 <= i + dx < n and 0 <= j + dy < m:
#             i += dx
#             j += dy

#     if board[i][j] == 1:
#         return True
#     else:
#         return False


# def move(dir, cnt):
#     for _ in range(cnt):
#         if dir == 0:
#             move_lst.append([0, -1])
#         elif dir == 1:
#             move_lst.append([0, 1])
#         elif dir == 2:
#             move_lst.append([-1, 0])
#         else:
#             move_lst.append([1, 0])


# def solution(n, m, x, y, queries):
#     answer = 0
#     board = [[0] * m for _ in range(n)]
#     board[x][y] = 1
#     for i, j in queries:
#         move(i, j)

#     for i in range(n):
#         for j in range(m):
#             if search(board, i, j, n, m):
#                 answer += 1

#     return answer


# print(solution(n, m, x, y, queries))


x = np.ones([n, m])

x[0] += x[1]
x[1] = np.zeros(m)

for i in range(n):
    x[i] +=

print(x)
