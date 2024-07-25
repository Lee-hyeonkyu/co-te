n = int(input())


def func(n):
    dp = [0] * n
    if n == 1:
        return 1
    if n == 2:
        return 2
    dp[1] = 2
    dp[2] = 3

    for i in range(3, n):
        dp[i] = dp[i - 2] + dp[i - 1]

    return dp[-1]


print(func(n) % 10007)
