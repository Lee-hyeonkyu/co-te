n, k = map(int, input().split())

lst = [list(input().split()) for _ in range(n)]


print(sorted(lst)[k-1][0], sorted(lst)[k-1][1])
