# n = int(input())

# dp = [0 for _ in range(n+1)]
# lst = [0 for _ in range(n+1)]

# for i in range(2, n+1):
#     dp[i] = dp[i-1]+1
#     lst[i] = i-1

#     if not i % 3 and dp[i] > dp[i//3]+1:
#         dp[i] = dp[i//3]+1
#         lst[i] = i//3
#     if not i % 2 and dp[i] > dp[i//2]+1:
#         dp[i] = dp[i//2]+1
#         lst[i] = i//2

# print(dp[n])
# print(n, end=' ')

# b_n = n

# while lst[b_n]:
#     print(lst[b_n], end=' ')
#     b_n = lst[b_n]


# 2


from collections import deque

k = int(input())
dyn = [1e9 for _ in range(k+1)]
root = [0 for _ in range(k+1)]
current = deque()
current.append((k, -1))
while current:
    n, count = current.popleft()
    if n == 1:
        dyn[n] = count + 1
        break
    for i in [n/2, n/3, n-1]:
        if int(i) == i:
            i = int(i)
            if count + 1 < dyn[i]:
                dyn[i] = count+1
                root[i] = n
                current.append((i, count+1))

print(root)
target = 1
ans = str(target)
while target != k:
    target = root[target]
    ans = str(target) + " " + ans
print(dyn[1])
print(ans)
