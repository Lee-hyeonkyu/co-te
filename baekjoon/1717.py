import sys

sys.setrecursionlimit(100000)
n, m = map(int, sys.stdin.readline().split())

lst = [i for i in range(n + 1)]


def find(x):
    if lst[x] != x:
        lst[x] = find(lst[x])
    return lst[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        lst[b] = a
    else:
        lst[a] = b


for _ in range(m):
    t, a, b = map(int, sys.stdin.readline().split())
    if t:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
    else:
        union(a, b)
