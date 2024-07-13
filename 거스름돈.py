def solution(n, money):
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in money:
        for j in range(1, n + 1):
            if j >= i:
                dp[j] += dp[j - i]

    return dp[-1]


n = 5
money = [1, 2, 5]

result = 4


print(solution(n, money) == result)
