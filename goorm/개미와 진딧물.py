def search(y, x, k):
    # 윗 부분 탐색
    for i in range(k, -1, -1):
        for j in range(-i, i+1):
            if 0 <= y - k + i < n and 0 <= x + j < n:
                #print (y -  k + i , x + j)
                if ant_matrix[y - k + i][x + j] == 2:
                    return True
    # 아랫부분 탐색
    for i in range(1, k+1):
        for j in range(-k + i, +k - i + 1):
            if 0 <= y + i < n and 0 <= x + j < n:
                #print (y + i , x + j)
                if ant_matrix[y + i][x + j] == 2:
                    return True
    return False


n, k = map(int, input().split())
ant_matrix = list()
for i in range(n):
    ant_matrix.append(list(map(int, input().split())))

ant_save = 0
# 개미의 값은 1이다. 즉 ant_matrix[i][j] == 1일때 search함수를 실행한다.
for i in range(n):
    for j in range(n):
        if ant_matrix[i][j] == 1:
            # 탐색해서 진딧물이 있으면 살아남은 개미로 생각한다.
            if search(i, j, k):
                ant_save += 1
print(ant_save)
