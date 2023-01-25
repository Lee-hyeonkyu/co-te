n = int(input())

d = [0] * 1_000_001

d[1] = 1
d[2] = 2


def dp(n):
    for i in range(3, n+1):
        if not d[i]:
            d[i] = (d[i-1] + d[i-2]) % 15746
    return d[n]


print(dp(n))
