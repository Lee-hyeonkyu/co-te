from collections import deque

n, m, k = map(int, input().split())
space = [[5] * n for _ in range(n)]
age_tree = [[deque() for _ in range(n)] for _ in range(n)]
A = [list(map(int, input().split())) for _ in range(n)]
