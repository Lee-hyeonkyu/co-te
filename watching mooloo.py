import sys

input = sys.stdin.readline

n, k = map(int, input().split())
days = list(map(int, input().split()))

cost = k + 1

for i in range(1, len(days)):
    if days[i] - days[i - 1] > k + 1:
        cost += k + 1
    else:
        cost += days[i] - days[i - 1]

print(cost)


# 금일 - 작일  vs (추가금+1)
