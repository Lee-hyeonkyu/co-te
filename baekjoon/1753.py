import sys
from queue import PriorityQueue

input = sys.stdin.readline

v, e = map(int, input().split())
start = int(input())

graph = [[] for _ in range(v)]  # |시작노드, 가중치, 도착노드|

visited = [float("inf") for _ in range(v)]


def dijkstra(start) -> None:
    pq = PriorityQueue()
    pq.put((0, start))  # |거리 , 정점|
    visited[start] = 0

    while not pq.empty():
        dist, curr = pq.get()

        if visited[curr] < dist:
            continue

        for weight, next_ in graph[curr]:
            next_dist = dist + weight
            if next_dist < visited[next_]:
                visited[next_] = next_dist
                pq.put((next_dist, next_))


for _ in range(e):
    x, y, z = map(int, input().split())

    graph[x - 1].append([z, y - 1])

dijkstra(start - 1)


for i in visited:
    if i == float("inf"):
        print("INF")
    else:
        print(i)
