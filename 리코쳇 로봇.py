from collections import deque

# 멈추는 조건 -> D가 있거나 배열 끝이거나
# BFS도 될듯?

board = ["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]


# def solution(board):
#     q = deque()
#     # 하, 우, 상, 좌
#     pos_ = ((1, 0), (0, 1), (-1, 0), (0, -1))
#     visited = [[0] * len(board[0]) for _ in range(len(board))]
#     # 시작 위치 값 넣기

#     for i in range(len(board)):
#         for j in range(len(board[0])):
#             if board[i][j] == "R":
#                 q.append([i, j])
#             elif board[i][j] == "G":
#                 goal = [i, j]
#     while q:
#         x, y = q.popleft()
#         for i in range(4):
#             nx = x + pos_[i][0]
#             ny = y + pos_[i][1]
#             while 1:
#                 if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
#                     if board[nx][ny] != "D":
#                         nx += pos_[i][0]
#                         ny += pos_[i][1]
#                     else:
#                         nx -= pos_[i][0]
#                         ny -= pos_[i][1]
#                         if not visited[nx][ny]:
#                             q.append([nx, ny])
#                             visited[nx][ny] = visited[x][y] + 1
#                         break
#                 else:
#                     break

#     for i in visited:
#         print(i)

#     answer = visited[goal[0]][goal[1]]
#     if answer:
#         return answer
#     else:
#         return -1


# print(solution(board))


def solution(board):
    q = deque()
    # 하, 우, 상, 좌
    pos_ = ((1, 0), (0, 1), (-1, 0), (0, -1))
    visited = [[0] * len(board[0]) for _ in range(len(board))]
    # 시작 위치 값 넣기

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "R":
                q.append([i, j])
                visited[i][j] = -999
            elif board[i][j] == "G":
                goal = [i, j]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + pos_[i][0]
            ny = y + pos_[i][1]
            while 1:
                if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
                    if board[nx][ny] == "D":
                        nx -= pos_[i][0]
                        ny -= pos_[i][1]
                        if not visited[nx][ny]:
                            q.append([nx, ny])
                            if visited[x][y] == -999:
                                visited[nx][ny] = 1
                            else:
                                visited[nx][ny] = visited[x][y] + 1
                        break
                    else:
                        nx += pos_[i][0]
                        ny += pos_[i][1]

                else:
                    nx -= pos_[i][0]
                    ny -= pos_[i][1]
                    if not visited[nx][ny]:
                        q.append([nx, ny])
                        if visited[x][y] == -999:
                            visited[nx][ny] = 1
                        else:
                            visited[nx][ny] = visited[x][y] + 1

                    break

    answer = visited[goal[0]][goal[1]]
    if answer:
        return answer
    else:
        return -1
