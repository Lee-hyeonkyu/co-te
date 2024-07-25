n = int(input())

arr = list(map(int, input().split()))

dp = [0] * n

dp[0] = 1
for i in range(1, n):
    tmp = 0
    for j in range(i):
        if arr[i] > arr[j]:
            tmp = max(dp[j], tmp)
    dp[i] = tmp + 1

print(max(dp))
