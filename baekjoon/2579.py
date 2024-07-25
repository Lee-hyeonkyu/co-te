stair = [int(input()) for _ in range(int(input()))]


def func(stair):
    n = len(stair)

    if n == 1:
        return stair[0]
    if n == 2:
        return stair[0] + stair[1]

    dp = [0] * (n + 1)

    dp[1] = stair[0]
    dp[2] = stair[0] + stair[1]

    for i in range(3, n + 1):
        dp[i] = max(dp[i - 2] + stair[i - 1], dp[i - 3] + stair[i - 2] + stair[i - 1])
    return dp[-1]


print(func(stair))

"""
a = 10, 20, 15, 25, 10, 20
dp = 0, 10, 30, 35, 55, 

10 + 15, 0 + 20 + 15  = 35
30 + 25 , 10 + 15 + 25 

"""
