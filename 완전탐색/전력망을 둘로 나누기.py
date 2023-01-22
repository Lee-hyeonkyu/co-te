from collections import deque
n = 9

wires = [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]


def bfs(a, visited, wire):
    q = deque([a])
    result = 1
    visited[a] = True

    while q:
        n = q.popleft()

        for i in wire[n]:
            if not visited[i]:
                result += 1
                q.append(i)
                visited[i] = True

    return result


def solution(n, wires):
    answer = n
    wire = [[] for _ in range(n+1)]

    for a, b in wires:
        wire[a].append(b)
        wire[b].append(a)

    for a, b in wires:
        visited = [False]*(n+1)
        visited[b] = True
        result = bfs(a, visited, wire)

        if abs(result - (n-result)) < answer:
            answer = abs(result - (n-result))

    return answer


print(solution(n, wires))
