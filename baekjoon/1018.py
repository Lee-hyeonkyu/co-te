n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

answer = 2500
# 색상 확인
check = ["W", "B"]

lim_n = n - 8
lim_m = m - 8

# 전체 반복문의 크기를 8개 칸으로 짤라서 0부터 시작
for i in range(lim_n + 1):
    for j in range(lim_m + 1):
        # w인지 b인지 확인할 변수
        cnt = 0
        cnt_chck_1, cnt_chck_2 = 0, 0
        # 주어진 값부터 +8칸까지 탐색
        for k in range(i, i + 8):
            # 한 줄 넘어 갈 때마다 순서가 바뀌니까 +1
            cnt += 1
            # 가로줄 탐색
            for h in range(j, j + 8):
                # 백흑 순서 탐색
                if board[k][h] == check[cnt % 2]:
                    cnt_chck_1 += 1
                # 흑백 순서 탐색
                if board[k][h] == check[(cnt + 1) % 2]:
                    cnt_chck_2 += 1
                cnt += 1
        # 값의 최소 값
        answer = min(min(cnt_chck_1, cnt_chck_2), answer)

print(answer)
