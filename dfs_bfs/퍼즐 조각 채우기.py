from collections import deque

# game_board = [
#     [1, 1, 0, 0, 1, 0],
#     [0, 0, 1, 0, 1, 0],
#     [0, 1, 1, 0, 0, 1],
#     [1, 1, 0, 1, 1, 1],
#     [1, 0, 0, 0, 1, 0],
#     [0, 1, 1, 1, 0, 0],
# ]
# table = [
#     [1, 0, 0, 1, 1, 0],
#     [1, 0, 1, 0, 1, 0],
#     [0, 1, 1, 0, 1, 1],
#     [0, 0, 1, 0, 0, 0],
#     [1, 1, 0, 1, 1, 0],
#     [0, 1, 0, 0, 0, 0],
# ]
game_board = [
    [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1],
    [0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1],
    [1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0],
    [1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0],
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0],
    [1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0],
    [0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
]
table = [
    [1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0],
    [1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1],
    [1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1],
    [0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1],
    [0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0],
    [1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1],
    [1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0],
    [1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1],
    [0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1],
]


# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def cutting(board):
    s_r = 100
    e_r = 0

    s_c = 100
    e_c = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1:
                s_r = min(s_r, i)
                s_c = min(s_c, j)
                e_r = max(e_r, i)
                e_c = max(e_c, j)

    board = board[s_r : e_r + 1]

    for i in range(len(board)):
        board[i] = board[i][s_c : e_c + 1]
    return board


def rotaion(board):
    new_board = []
    for j in range(len(board[0])):
        tmp = []
        for i in range(len(board) - 1, -1, -1):
            tmp.append(board[i][j])
        new_board.append(tmp)
    return new_board


def get_piece(q, table):
    visited = [[0] * len(table[0]) for _ in range(len(table))]

    while q:
        x, y = q.popleft()
        visited[x][y] = 1
        table[x][y] = 0
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if (
                0 <= nx < len(table[0])
                and 0 <= ny < len(table)
                and table[nx][ny]
                and not visited[nx][ny]
            ):
                visited[nx][ny] = 1
                table[nx][ny] = 0
                q.append([nx, ny])
    return visited


def find(board):
    q = deque()
    lst = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1:
                q.append([i, j])
                piece = cutting(get_piece(q, board))
                lst.append(piece)
    return lst


def solution(game_board, table):
    answer = 0
    for i in range(len(game_board)):
        for j in range(len(game_board[0])):
            if game_board[i][j] == 0:
                game_board[i][j] = 1
            else:
                game_board[i][j] = 0

    pieces = find(table)
    board_set = find(game_board)

    for i in range(len(pieces)):
        collect = 0
        piece = pieces[i]

        for j in range(len(board_set)):
            match_pi = board_set[j]
            for _ in range(4):
                if piece == match_pi:
                    collect = 1
                    break
                piece = rotaion(piece)
            if collect:
                del board_set[j]
                for h in piece:
                    answer += sum(h)
                break

    return answer


print(solution(game_board, table))
