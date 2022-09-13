computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
n = 3


def dfs(n, computers, i, visited):
    visited[i] = True
    for j in range(n):
        if j != i and computers[i][j] == 1:
            if visited[j] == False:
                dfs(n, computers, j, visited)


def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]
    for i in range(n):
        if visited[i] == False:
            dfs(n, computers, i, visited)
            answer += 1
    return answer


print(solution(n, computers))
