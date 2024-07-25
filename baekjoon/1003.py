# def fibonacci(n) -> int:
#     global zero, one
#     if n == 0:
#         zero += 1
#         return 0
#     elif n == 1:
#         one += 1
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)


# for _ in range(int(input())):
#     zero = 0
#     one = 0
#     fibonacci(int(input()))
#     print(zero, one)

import sys

t = int(sys.stdin.readline())

memo = [[1, 0], [0, 1], [1, 1]]

for i in range(3, 41):
    x1, y1 = memo[-1]
    x2, y2 = memo[-2]
    memo.append([x1 + x2, y1 + y2])

for _ in range(t):
    n = int(sys.stdin.readline())
    print(*memo[n])
