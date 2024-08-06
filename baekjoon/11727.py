import sys

dp = [0] * 1001


dp[1] = 1
dp[2] = 3

x = int(sys.stdin.readline())

for i in range(3, x + 1):
    dp[i] = dp[i - 1] + dp[i - 2] * 2

print(dp[x] % 10007)
