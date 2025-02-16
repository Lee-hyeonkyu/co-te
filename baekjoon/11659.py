n, m = map(int, input().split())
arr = tuple(map(int, input().split()))


S = [arr[0]]

for i in range(1, n):
    S.append(S[i - 1] + arr[i])

for _ in range(m):
    i, j = map(int, input().split())
    if i > 1:
        print(S[j - 1] - S[i - 2])
    else:
        print(S[j - 1])
