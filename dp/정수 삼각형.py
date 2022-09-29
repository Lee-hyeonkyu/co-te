triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]


def solution(triangle):
    n = len(triangle)
    dp = [[0]*n for _ in range(n)]
    dp[0][0] = triangle[0][0]
    print(dp)
    for y in range(n-1):
        for x in range(len(triangle[y])):
            dp[y+1][x] = max(dp[y+1][x], dp[y][x] + triangle[y+1][x])
            dp[y+1][x+1] = max(dp[y+1][x+1], dp[y][x] + triangle[y+1][x+1])

    return max(dp[-1])


print(solution(triangle))
