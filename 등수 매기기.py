import sys

input = sys.stdin.readline
n = int(input())
cnt = 0
lst = []

for i in range(n):
    lst.append(int(input()))
lst.sort()

for i in range(n):
    cnt += abs(lst[i] - (i + 1))

print(cnt)
