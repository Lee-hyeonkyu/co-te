import sys

n = int(sys.stdin.readline())

lst = [sys.stdin.readline().rstrip() for _ in range(n)]
lst = list(set(lst))
lst.sort(key=lambda x: (len(x), x))
print("\n".join(lst))
