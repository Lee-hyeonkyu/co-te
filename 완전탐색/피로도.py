k = 80
dungeons = [[80, 20], [50, 40], [30, 10]]


def dfs(k, cnt, answer, dungeons, visited):
    if cnt > answer:
        answer = cnt
    for i in range(len(dungeons)):
        if k >= dungeons[i][0] and not visited[i]:
            visited[i] = 1
            answer = dfs(k - dungeons[i][1], cnt+1, answer, dungeons, visited)
            visited[i] = 0
    return answer


def solution(k, dungeons):
    answer = 0
    visited = [0] * len(dungeons)
    answer = dfs(k, 0, answer, dungeons, visited)
    return answer


print(solution(k, dungeons))
