from itertools import combinations
'''
어떻게 하면 쓸모없는 치킨집을 없앨 수 있을까?
어떤 치킨집을 제거해야하나
조합으로 전부 찾기
'''
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

zib = []  # 집
dak = []  # 치킨
answer = 9999
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:  # 집 위치 저장
            zib.append((i, j))
        elif board[i][j] == 2:  # 치킨 위치 저장
            dak.append((i, j))


for i in combinations(dak, m):
    y = 0  # 조합 하나에 대해서 초기화
    for j in zib:
        x = 9999  # 최대값
        for k in range(m):
            x = min(x, abs(j[0]-i[k][0]) + abs(j[1] - i[k][1]))  # 최단거리
        y += x  # 최단거리저장
    answer = min(answer, y)  # 전체중 최단거리
print(answer)
