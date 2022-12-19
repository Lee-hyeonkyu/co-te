n, k = map(int, input().split())


l = 1004
ans = 0

area = [[0 for _ in range(l)] for _ in range(l)]

for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    area[y1][x1] += 1
    area[y1][x2] -= 1
    area[y2][x1] -= 1
    area[y2][x2] += 1


for i in range(l):
    for j in range(1, l):
        area[i][j] += area[i][j-1]


for j in range(l):
    for i in range(1, l):
        area[i][j] += area[i-1][j]

for i in range(l):
    for j in range(l):
        if area[i][j] == k:
            ans += 1

print(ans)
