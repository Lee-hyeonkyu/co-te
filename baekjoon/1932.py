n = int(input())


def func(n):
    arr = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0] * (i + 1) for i in range(n)]
    dp[0] = arr[0]
    if n == 1:
        return arr[-1][0]

    for i in range(n - 1):  # 전체 길이 반복
        for j in range(len(arr[i])):  # 현재 보는 arr의 층의 값들
            up_num = dp[i][j]
            for k in range(j, j + 2):
                if dp[i + 1][k] == 0:
                    dp[i + 1][k] = up_num + arr[i + 1][k]
                else:
                    dp[i + 1][k] = max(dp[i + 1][k], up_num + arr[i + 1][k])

    return max(dp[-1])


print(func(n))
