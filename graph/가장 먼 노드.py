from collections import deque, defaultdict


edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
n = 6


def bfs(start, table, visited):
    q = deque()
    q.append((start, 0))
    visited.add(start)
    n = defaultdict(lambda: 0)
    while q:
        node, cnt = q.popleft()
        visited.add(node)
        print('visited:', visited)
        for i in table[node]:
            print('i:', i)
            if i not in visited:
                visited.add(i)
                n[cnt + 1] += 1
                q.append((i, cnt + 1))
                print("q:", q)
                print('n:', n)
    return n[cnt]


def solution(n, edge):
    table = defaultdict(set)
    visited = set()

    for i, j in edge:
        table[i].add(j)
        table[j].add(i)
    print('table:', table)

    answer = bfs(1, table, visited)

    return answer


print(solution(n, edge))
