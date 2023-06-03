from collections import deque

maps = ["SOOOL", "XXXXO", "OOOOO", "OXXXX", "OOOOE"]


def bfs(q, board, dx, dy, maps):
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (
                0 <= nx < len(board)
                and 0 <= ny < len(board[0])
                and not board[nx][ny]
                and maps[nx][ny] != "X"
            ):
                board[nx][ny] += board[x][y] + 1
                q.append([nx, ny])
    return board


def solution(maps):
    q = deque()
    dx = [1, 0, 0, -1]
    dy = [0, 1, -1, 0]
    answer = 0
    n = len(maps)
    m = len(maps[0])
    board = [[0] * m for _ in range(n)]
    q.append(*[[i, j] for i in range(n) for j in range(m) if maps[i][j] == "S"])
    bfs(q, board, dx, dy, maps)

    for i in range(n):
        for j in range(m):
            if maps[i][j] == "L":
                lev = board[i][j]
                lev_pos = [i, j]
    if not lev:
        return -1
    board = [[0] * m for _ in range(n)]
    board[lev_pos[0]][lev_pos[1]] = lev
    q.append(lev_pos)
    bfs(q, board, dx, dy, maps)
    answer = [board[i][j] for i in range(n) for j in range(m) if maps[i][j] == "E"][0]
    if not answer:
        return -1
    return answer


print(solution(maps))
