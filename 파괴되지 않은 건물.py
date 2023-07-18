board = [[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]]
skill = [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]


def solution(board, skill):
    answer = 0
    lst = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]

    for i in skill:
        size = i[-1]
        if i[0] == 1:
            type = -1
        else:
            type = 1
        # 시작
        lst[i[1]][i[2]] += size * type
        # 시작점 끝
        lst[i[1]][i[4] + 1] -= size * type
        # 끝점 시작
        lst[i[3] + 1][i[2]] -= size * type
        # 끝
        lst[i[3] + 1][i[4] + 1] += size * type

    for i in range(len(board)):
        for j in range(1, len(board[0])):
            lst[i][j] += lst[i][j - 1]

    for i in range(len(board[0])):
        for j in range(1, len(board)):
            lst[j][i] += lst[j - 1][i]
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += lst[i][j]
            if board[i][j] > 0:
                answer += 1
    return answer


print(solution(board, skill))
