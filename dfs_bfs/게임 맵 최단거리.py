from collections import deque
import copy

maps = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [
    1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]


def solution(maps):
    # 테스트 19 실패(런타임)
    # if (maps[-1][-2] == 0) and (maps[-2][-2:] == [0, 0]):
    #     return -1
    map = copy.deepcopy(maps)
    n = len(maps)
    m = len(maps[0])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((0, 0))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if map[nx][ny] == 0:
                continue
            if map[nx][ny] == 1:
                map[nx][ny] = map[x][y] + 1
                queue.append((nx, ny))
    print(map)
    if map[n-1][m-1] == 1:
        answer = -1
    else:
        answer = map[n-1][m-1]
    return answer


print(solution(maps))
