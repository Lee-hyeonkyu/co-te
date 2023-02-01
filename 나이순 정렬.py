import sys

n = int(sys.stdin.readline())
lst = [list(sys.stdin.readline().split()) for _ in range(n)]

tmp = []
for i in zip(range(n), lst):
    i[1][0] = int(i[1][0])
    tmp.append(i)


tmp.sort(key=lambda x: (x[1][0], x[0]))
for x, y in tmp:
    print(*y)
