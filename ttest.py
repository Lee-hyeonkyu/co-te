import numpy as np
n, m = map(int, input().split())

x = np.array([list(map(int, input().split()))for _ in range(n)])
y = np.array([list(map(int, input().split()))for _ in range(n)])
for i in x+y:
    print(*i)
