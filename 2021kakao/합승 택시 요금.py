n = 6
s = 4
a = 6
b = 2
fares = [[4, 1, 10],
         [3, 5, 24],
         [5, 6, 2],
         [3, 1, 41],
         [5, 1, 24],
         [4, 6, 50],
         [2, 4, 66],
         [2, 3, 22],
         [1, 6, 25]]


def floyd(dist, n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if dist[j][i] + dist[i][k] < dist[j][k]:
                    dist[j][k] = dist[j][i] + dist[i][k]


def solution(n, s, a, b, fares):
    INF = 200 * 100000
    dist = [[INF for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for edge in fares:
        dist[edge[0]-1][edge[1]-1] = edge[2]
        dist[edge[1]-1][edge[0]-1] = edge[2]

    floyd(dist, n)
    s -= 1
    a -= 1
    b -= 1
    answer = INF

    for k in range(n):
        answer = min(answer, dist[s][k] + dist[k][a] + dist[k][b])

    return answer


print(solution(n, s, a, b, fares))
