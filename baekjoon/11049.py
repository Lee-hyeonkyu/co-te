# import sys

# n = int(sys.stdin.readline())

# mat = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# check = [0] * n

# for i, j in enumerate(range(n - 1)):
#     print(i + 1, mat[j], mat[j + 1])

n = 3
dp = [[987654321] * (n + 1) for _ in range(n + 1)]


print(dp)


for i in range(1, n + 1):
    dp[i][i] = 0

print()
for i in dp:
    print(i)
