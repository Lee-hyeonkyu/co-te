drawing_paper = [[0]*100 for _ in range(100)]


for i in range(int(input())):
    x, y = map(int, input().split())
    for j in range(x, x+10):
        for h in range(y, y+10):
            drawing_paper[j][h] += 1

cnt = 0

for i in range(100):
    for j in range(100):
        if drawing_paper[i][j]:
            cnt += 1

print(cnt)
