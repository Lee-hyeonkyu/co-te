grid = ["SL", "LR"]


# 상 좌 하 우
# dir = [[-1, 0], [0, -1], [1, 0], [0, 1]]
# "R"
# print([dir[-1]] + dir[:-1])
# "L"
# print(dir[1:] + [dir[0]])
# board = [(len(grid[0]) * 2 + 1) * [[]] for _ in range(len(grid) * 2 + 1)]


def tlpo(board, nx, ny):
    # nx가 끝일 때
    if nx == 0:
        nx = len(board) - 1
    elif nx == len(board) - 1:
        nx = 0
    # ny가 끝일 때
    if ny == 0:
        ny = len(board[0]) - 1
    elif ny == len(board[0]) - 1:
        ny = 0
    return nx, ny


def rotate(change, dir):
    if change == "R":
        dir = [dir[-1]] + dir[:-1]
    elif change == "L":
        dir = dir[1:] + [dir[0]]
    return dir


def dfs(board, x, y, cnt, dir):
    dx, dy = dir[0]
    nx = dx + x
    ny = dy + y
    print(nx, ny)
    # 배열 안 체크
    if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
        if (nx % 2) and (ny % 2):
            cnt += 1
            dir = rotate(board[nx][ny], dir)
        else:
            #  공간에 방향으로 갔던 기록이 없다면 저장
            if dir[0] not in board[nx][ny]:
                board[nx][ny].append(dir[0])
                # 저장뒤 그 위치가 배열 끝라인이라면 위치 이동
                if (nx == 0 or nx == len(board) - 1) or (
                    ny == 0 or ny == len(board[0]) - 1
                ):
                    nx, ny = tlpo(board, nx, ny)  ## 여기서 한칸을 넘어가버리는 상황이 발생.
            else:
                return cnt

        dfs(board, nx, ny, cnt, dir)
    return cnt


def solution(grid):
    global dir
    words = "".join(grid)
    words = iter(words)
    # board init
    board = [(len(grid[0]) * 2 + 1) * [[]] for _ in range(len(grid) * 2 + 1)]
    for i in range(1, len(board), 2):
        for j in range(1, len(board[0]), 2):
            board[i][j] = next(words)
    answer = []

    # 시작 네방향 체크
    for i in range(4):
        print("###@@")
        dir = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        dir = dir[-i:] + dir[:-i]
        cnt = dfs(board, 1, 1, 0, dir)
        # 한번이라도 안간 방향이 있다면 추가
        if cnt:
            answer.append(cnt)

    # start
    answer.sort()
    return answer


print(solution(grid))
