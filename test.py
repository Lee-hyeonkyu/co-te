import sys
input = sys.stdin.readline


def star(n):
    if n == 3:
        return ["***", "* *", "***"]

    S = star(n//3)
    L = []

    for i in S:
        L.append(i*3)
    for i in S:
        L.append(i + " "*(n//3) + i)
    for i in S:
        L.append(i*3)
    return L


n = int(input())
print("\n".join(star(n)))
