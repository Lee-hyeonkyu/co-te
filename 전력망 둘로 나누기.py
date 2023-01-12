from collections import deque

n = 9
wires = [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]

# 완탐


def bfs(a, b, visited, tree):
    result = 1
    visited[a] = True
    visited[b] = True
    q = deque([a])

    while q:
        node = q.popleft()
        for i in tree[node]:
            if not visited[i]:
                result += 1
                q.append(i)
                visited[i] = True

    return result


def solution(n, wires):
    answer = n
    # 양방향 연결해줄 공간 만들기
    tree = [[] for _ in range(n+1)]

    # wires의 리스트를 tree라는 2중 리스트에 리스트 인덱스마다 연결된 값 할당하기.
    for a, b in wires:
        tree[a].append(b)
        tree[b].append(a)

    # 다시 리스트를 돌면서 하나씩 끊으며 노드 개수 확인할 예정.
    for a, b in wires:
        # 방문리스트를 만들어서 방문했다면 다시 방문하지 못하도록 함.
        visited = [False] * (n+1)
        result = bfs(a, b, visited, tree)

        answer = min(abs(n-result-result), answer)

    return answer


print(solution(n, wires))
