rows = 6
columns = 6
queries = [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]


def solution(rows, columns, queries):

    answer = []
    board = [[0 for _ in range(columns)] for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            board[i][j] = (j+1)+i*columns

    for i in queries:
        x1, y1, x2, y2 = i
        x1 = x1-1
        y1 = y1-1
        x2 = x2-1
        y2 = y2-1
        tmp = board[x1][y1]
        mini = tmp

        for i in range(x1, x2):
            move = board[i+1][y1]
            board[i][y1] = move
            mini = min(mini, move)

        for i in range(y1, y2):
            move = board[x2][i+1]
            board[x2][i] = move
            mini = min(mini, move)

        for i in range(x2, x1, -1):
            move = board[i-1][y2]
            board[i][y2] = move
            mini = min(mini, move)

        for i in range(y2, y1, -1):
            move = board[x1][i-1]
            board[x1][i] = move
            mini = min(mini, move)

        board[x1][y1+1] = tmp
        answer.append(mini)

    return answer
