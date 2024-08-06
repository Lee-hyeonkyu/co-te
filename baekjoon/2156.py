import sys

n = int(sys.stdin.readline())


def func(n):

    wine = [int(sys.stdin.readline()) for _ in range(n)]
    if n == 1:
        return wine[0]
    if n == 2:
        return wine[0] + wine[1]

    max_drink = [0] * n
    max_drink[0] = wine[0]
    max_drink[1] = wine[1] + max_drink[0]

    for i in range(2, n):
        max_drink[i] = max(
            max_drink[i - 3] + wine[i - 1] + wine[i],
            max_drink[i - 2] + wine[i],
            max_drink[i - 1],
        )
    return max_drink[-1]


print(func(n))


"""
dp[3] = dp[3-3] + wine[3-1] + wine[3], dp[3-2]+ wine[3]


dp[i] = max(dp[i-3] + wine[i-1] + wine[i], dp[i-2] + wine[i])
dp[3] = 25


dp[4] = dp[4-3] + wine[3] + wine[4] , dp[4-2] + wine[4]
dp[4] = 16 + 9 + 8 , 23 + 8
dp[4] = 33


dp[5] = dp[2] + wine[4] + wine[5], dp[3] + wine[5]
 =  23 + 8 + 1,  28 + 1 
"""
