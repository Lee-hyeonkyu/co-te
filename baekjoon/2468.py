from collections import deque

n = int(input())


board = [list(map(int, input().split())) for _ in range(n)]


dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]

answer = [1]


q = deque()
for rain in range(1, 101):
    visited = [[0] * n for _ in range(n)]
    tmp = 0
    # 안전지역 찾기
    for i in range(n):
        for j in range(n):
            if board[i][j] > rain and visited[i][j] == 0:
                q.append([i, j])
                visited[i][j] = 1
                tmp += 1
                while q:
                    x, y = q.popleft()
                    for idx in range(4):
                        nx = dx[idx] + x
                        ny = dy[idx] + y

                        if (
                            0 <= nx < n
                            and 0 <= ny < n
                            and visited[nx][ny] == 0
                            and board[nx][ny] > rain
                        ):
                            q.append([nx, ny])
                            visited[nx][ny] = 1
    answer.append(tmp)
print(max(answer))


######################## union-find

import sys
from collections import defaultdict

root = {}


def find(x):
    """
    목표: x의 root를 찾는다.
    - 경로압축: x에서 root까지의 모든 노드의 root를 찾는다.
      (path의 모든 노드들을 저장해놓고, root를 할당하는 것과 같다.)
    """
    if root[x] == x:
        return x
    root[x] = find(root[x])
    return root[x]


def union(r1, r2):
    """
    목표: 두 root를 하나로 합친다. (r2를 r1 아래에 둔다.)
    """
    root[find(r2)] = find(r1)


def adj(p, W):
    # 하 좌 우 상
    yield p - W
    yield p - 1
    yield p + 1
    yield p + W


def main():
    # 1. 데이터 입력 및 가공
    input = sys.stdin.readline

    # 패딩을 위해 P와 W를 사용한다.
    # 4방향의 이웃들에 대해, 패딩인 이웃은 무시하고 넘어가게 된다.
    N = int(input())  # 원래 한 열의 크기
    P = 1  # 4방향 패딩 크기
    W = N + 2 * P  # 패딩된 한 열의 크기

    h2i = defaultdict(list)  # 높이별 위치의 인덱스들
    for r in range(P, N + P):
        heights_line = list(map(int, input().split()))
        for h, i in zip(heights_line, range(r * W + 1, (r + 1) * W - 1)):
            h2i[h].append(i)
    heights = sorted(h2i, reverse=True)

    heights.pop()  # 최저 높이 heights[-1]에 대해서는 모두 잠기지 않음, cnt = 1 (= min_cnt)
    cnt = 1
    rep = []
    for h in heights:  # 물의 높이 = h - 1
        # root 초기화
        for i in h2i[h]:
            root[i] = i
        for i in h2i[h]:
            for j in adj(i, W):
                if j in root:
                    union(i, j)

        rep = [i for i in rep if root[i] == i]
        print(rep)
        for i in h2i[h]:
            if root[i] == i:
                rep.append(i)
        print("@@@")
        print(rep)
        print("@@")


print(main())
