<<<<<<< HEAD
import numpy as np
n, m = map(int, input().split())

<<<<<<< HEAD
# x = [1, 6, 10, 2, 1, 5, 2]
# # x = [1, 2, 3, 10, 5, 4, 2]
# # x = [1, 10, 6, 3, 4, 1, 2]
# # x = [6, 8, 4]
# # x = [1, 10, 3, 1]
# # x = [1, 1, 1, 2000]
# while 1:
#     m = sum(x)/len(x)
#     if x[-1] < m:
#         x = x[:-1]
#         print(x)
#     else:
#         x[-1] >= m
#         if m < x[-2] + x[-1] - m:


# m = sum(x)/len(x)
# print(math.ceil(m))

# n = 10
# for i in [n/2, n/3, n-1]:
#     if int(i) == i:
#         print(True)
#     else:
#         print(False)


import sys
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


target = 1
ans = str(target)
while target != k:
    target = root[target]
    ans = str(target) + " " + ans
print(dyn[1])
print(ans)
=======
x = np.array([list(map(int, input().split()))for _ in range(n)])
y = np.array([list(map(int, input().split()))for _ in range(n)])
for i in x+y:
    print(*i)
>>>>>>> 873c90f41b309d7b349a83daf09bf7f2fd9d118e
=======
print(24//1)
>>>>>>> 76a3a6a (.)
