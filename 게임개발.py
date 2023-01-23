n, m = map(int, input().split())
x, y, d = map(int, input().split())
board = [list(map(int, input().split()))for _ in range(n)]
visited = [[0]*m for _ in range(n)]


def turn_left(direction):
    direction -= 1
    if direction == -1:
        direction = 3

    return direction


def solution(board, visited, x, y, d):
    # Counterclockwise
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    # Current position check
    visited[x][y] = 1
    # 4 Direction check
    check_t = 0
    # Counting(check start position +1)
    cnt = 1

    while 1:
        # Turn left
        d = turn_left(d)
        # Move
        nx = x + dx[d]
        ny = y + dy[d]
        # Make sure it's land and when not visited it
        if not visited[nx][ny] and not board[nx][ny]:
            visited[nx][ny] = 1
            x = nx
            y = ny
            cnt += 1
            # Initialize check_t
            check_t = 0
            continue
        else:
            check_t += 1

        # Already visited or if it's the sea
        if check_t == 4:
            nx = x - dx[d]
            ny = y - dy[d]
            # Undo
            if not board[nx][ny]:
                x = nx
                y = ny
            else:
                break
            check_t = 0

    return cnt


print(solution(board, visited, x, y, d))
