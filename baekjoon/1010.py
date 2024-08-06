import sys


def fac(x):
    f = 1
    for i in range(x):
        f *= i + 1

    return f


matrix = [[0] * 30 for _ in range(30)]

matrix[0] = [i + 1 for i in range(30)]

for i in range(1, 30):
    for j in range(1, 30):
        matrix[i][j] = matrix[i - 1][j - 1] + matrix[i][j - 1]

t = int(sys.stdin.readline())


for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    print(fac(m) // (fac(n) * fac(m - n)))
    print(matrix[n - 1][m - 1])
