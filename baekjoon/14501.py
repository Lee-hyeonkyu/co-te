import sys

t = int(sys.stdin.readline())
date = []
price = []
for k in range(t):
    i, j = map(int, sys.stdin.readline().split())
    date.append(i)
    if k + i > t:
        price.append(0)
    else:
        price.append(j)

money = [price[-1]]

for i in range(2, t + 1):

    if date[-i] == 1:
        money.append(money[-1] + price[-i])
    elif date[-i] == len(money) + 1:
        money.append(max(money[-1], price[-i]))
    elif date[-i] > len(money):
        money.append(money[-1])
    else:
        money.append(max(money[-1], money[-(date[-i])] + price[-i]))

print(money[-1])


"""

 5,  4,  3,  2,  1,  1,  2,  3, 4, 5
50, 40, 30, 20, 10, 10, 20, 30, 0, 0



0 0 30 30 40 50 60 70 80 90 
"""


n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
dp = [0] * (n + 1)
for i in range(n - 1, -1, -1):
    if i + data[i][0] <= n:
        dp[i] = max(dp[i + data[i][0]] + data[i][1], dp[i + 1])
    else:
        dp[i] = dp[i + 1]

print(max(dp))
