from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(board, dir):
    n = len(board)
    price = [[99999] * n for _ in range(n)]
    price[0][0] = 0
    q = deque()
    q.append([0, 0, 0, dir])
    while q:
        x, y, cost, pos = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            past = i
            if 0 <= nx < n and 0 <= ny < n and not board[nx][ny]:
                if past == pos:
                    new_cost = cost + 100
                else:
                    new_cost = cost + 600
                if new_cost < price[nx][ny]:
                    price[nx][ny] = new_cost
                    q.append([nx, ny, new_cost, i])
    for i in price:
        print(i)

    return price[-1][-1]
    
def solution(board):
    return min(bfs(board, 0), bfs(board, 1))