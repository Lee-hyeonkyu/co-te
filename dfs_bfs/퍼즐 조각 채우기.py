from collections import deque
import copy


game_board = [[1, 1, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0], [0, 1, 1, 0, 0, 1], [
    1, 1, 0, 1, 1, 1], [1, 0, 0, 0, 1, 0], [0, 1, 1, 1, 0, 0]]

table = [[1, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 1, 1],
         [0, 0, 1, 0, 0, 0], [1, 1, 0, 1, 1, 0], [0, 1, 0, 0, 0, 0]]

n = len(game_board)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    for j in range(n):
        if table[i][j] == 1:
            table[i][j] = 0
        else:
            table[i][j] = 1


def bfs(board, space):
    visited = [[0]*n for _ in range(n)]
    q = deque()
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0 and visited[i][j] == 0:
                q.append([i, j])
                visited[i][j] = 1
                while q:
                    x, y = q.popleft()
                    space.append([x, y])
                    for idx in range(4):
                        nx = x + dx[idx]
                        ny = y + dy[idx]
                        if 0 <= nx < n and 0 <= ny < n:
                            if board[nx][ny] == 0 and visited[nx][ny] == 0:
                                q.append([nx, ny])
                                visited[nx][ny] = 1
    return space


def quad_shape(shape):
    tmp = []
    m_x, m_y = n, n
    for i in shape:
        m_x = min(m_x, i[0])
        m_y = min(m_y, i[1])

    for x, y in shape:
        tmp.append([x-m_x, y-m_y])
    return sorted(tmp)


def setting(space):
    cnt, shape, blank = 0, [], []
    for i in range(n):
        if space[i] == 99:
            print(space[cnt:i])
            shape.append(space[cnt:i])
            cnt += 1

    for i in shape:
        blank.append(quad_shape(*shape))

    return blank


def rotate(space):
    space = list(map(list, zip(*space[::-1])))

    return space


def solution(game_board, table):
    # 보드의 빈칸
    answer, board_blank, table_piece = [], [], []

    board_blank = bfs(game_board, board_blank)
    table_piece = bfs(table, table_piece)

    set_board_blank = setting(board_blank)
    set_table_piece = setting(table_piece)
    g_check = [0] * len(set_board_blank)

    for i in range(len(set_board_blank)):
        if set_board_blank[i] in set_table_piece and not g_check[i]:
            g_check[i] = 1
            set_table_piece.remove(set_board_blank[i])
            answer.append(set_board_blank[i])
        elif not g_check[i]:
            tmp_shape = copy.deepcopy(set_board_blank[i])
            for _ in range(4):
                tmp_shape = rotate(tmp_shape)
                if tmp_shape in set_table_piece and g_check[i] == False:
                    g_check[i] = True
                    set_table_piece.remove(tmp_shape)
                    answer.append(set_board_blank[i])
                    break

    cnt = 0
    for i in answer:
        cnt += len(i)

    return cnt


print(solution(game_board, table))

# 어딘가 리스트가 중첩이 됐다 그것을 풀어라.
