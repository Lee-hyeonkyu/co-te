# from collections import deque

# n = int(input())

# graph = sorted([sorted(list(map(int, input().split()))) for _ in range(int(input()))])

# q = deque([1])
# infection = set()
# check = []

# while q:
#     x = q.popleft()

#     for i in range(len(graph)):
#         if x in graph[i] and i not in check:
#             if graph[i][0] == x:
#                 q.append(graph[i][1])
#                 infection.add(graph[i][1])
#             else:
#                 q.append(graph[i][0])
#                 infection.add(graph[i][0])
#             check.append(i)

# print(len(infection))


import sys

n = int(sys.stdin.readline())
v = int(sys.stdin.readline())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
count = 0
for i in range(v):
    a, b = map(int, sys.stdin.readline().split())
    graph[a] += [b]
    graph[b] += [a]


def dfs(v):
    visited[v] = True
    global count
    count += 1
    for j in graph[v]:
        if not visited[j]:
            dfs(j)


dfs(1)
print(count - 1)


# [[1, 2], [1, 5], [2, 3], [2, 5], [4, 7], [5, 6]]
