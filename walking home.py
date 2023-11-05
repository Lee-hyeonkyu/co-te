import sys

input = sys.stdin.readline

T = int(input())
result = []
for _ in range(T):
    N, K = map(int, input().split())
    graph = [
        [True if char == "." else False for char in list(input()[:-1])]
        for _ in range(N)
    ]
    dp = [
        [
            {"D": [0 for _ in range(K + 1)], "R": [0 for _ in range(K + 1)]}
            for _ in range(N)
        ]
        for _ in range(N)
    ]
    dp[0][0]["D"][0] = 1
    dp[0][0]["R"][0] = 1
    for i in range(1, N):
        if graph[0][i]:
            dp[0][i]["R"][0] = dp[0][i - 1]["R"][0]
        if graph[i][0]:
            dp[i][0]["D"][0] = dp[i - 1][0]["D"][0]

    for k in range(K):
        for i in range(1, N):
            for j in range(1, N):
                if graph[i][j]:
                    dp[i][j]["D"][k] += dp[i - 1][j]["D"][k]
                    dp[i][j]["D"][k + 1] += dp[i - 1][j]["R"][k]
                    dp[i][j]["R"][k] += dp[i][j - 1]["R"][k]
                    dp[i][j]["R"][k + 1] += dp[i][j - 1]["D"][k]
    for i in range(1, N):
        for j in range(1, N):
            if graph[i][j]:
                dp[i][j]["D"][K] += dp[i - 1][j]["D"][K]
                dp[i][j]["R"][K] += dp[i][j - 1]["R"][K]

    for i in dp:
        print(i)
    print(sum(dp[-1][-1]["D"]) + sum(dp[-1][-1]["R"]))
################


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    board = [input() for _ in range(n)]
    answer = 0

    if k >= 1:
        up_right = True
        down_left = True
        for i in range(n):
            if board[0][i] == "H" or board[i][n - 1] == "H":
                up_right = False
            if board[i][0] == "H" or board[n - 1][i] == "H":
                down_left = False
        answer += up_right
        answer += down_left

    if k >= 2:
        for j in range(1, n - 1):
            check = True
            for i in range(n):
                if board[i][j] == "H":
                    check = False
                if i < j and board[0][i] == "H":
                    check = False
                if i > j and board[n - 1][i] == "H":
                    check = False
            answer += check

        for i in range(1, n - 1):
            check = True
            for j in range(n):
                if board[i][j] == "H":
                    check = False
                if j < i and board[j][0] == "H":
                    check = False
                if j > i and board[j][n - 1] == "H":
                    check = False
            answer += check

    if k >= 3:
        for i in range(1, n - 1):
            for j in range(1, n - 1):
                check = board[i][j] == "."
                for a in range(n):
                    if a <= i and board[a][j] == "H":
                        check = False
                    if a >= i and board[a][n - 1] == "H":
                        check = False
                    if a <= j and board[0][a] == "H":
                        check = False
                    if a >= j and board[i][a] == "H":
                        check = False
                answer += check

                check = board[i][j] == "."
                for a in range(n):
                    if a <= i and board[a][0] == "H":
                        check = False
                    if a >= i and board[a][j] == "H":
                        check = False
                    if a <= j and board[i][a] == "H":
                        check = False
                    if a >= j and board[n - 1][a] == "H":
                        check = False
                answer += check

    print(answer)
