# # answer = 0
# # s = 8


# # def check(pos, board):
# #     n, m = pos

# #     if board[n][m] == 0:
# #         board[n][m] = 1
# #         for i in range(s):
# #             board[n][i] = 1
# #             board[i][m] = 1
# #             if 0 <= n + i < s and 0 <= m + i < s:
# #                 board[n + i][m + i] = 1
# #             if 0 <= n + i < s and 0 <= m - i < s:
# #                 board[n + i][m - i] = 1
# #             if 0 <= n - i < s and 0 <= m + i < s:
# #                 board[n - i][m + i] = 1
# #             if 0 <= n - i < s and 0 <= m - i < s:
# #                 board[n - i][m - i] = 1
# #         return board, False
# #     else:
# #         return board, True


# # def bt(lst):
# #     global answer
# #     board = [[0] * s for _ in range(s)]
# #     if len(lst) == s:
# #         for pos in lst:
# #             board, switch = check(pos, board)
# #             if switch:
# #                 return
# #         answer += 1
# #         return

# #     for i in range(s):
# #         for j in range(s):
# #             if not lst or (
# #                 [i, j] not in lst
# #                 and (i > lst[-1][0] or (i == lst[-1][0] and j > lst[-1][1]))
# #             ):
# #                 lst.append([i, j])
# #                 bt(lst)
# #                 lst.pop()


# # bt([])
# # print(answer)

import sys

sys.setrecursionlimit(10**4)


def queen(lst, qn, idx):
    global answer
    switch = 0
    if qn == idx:
        answer += 1
        return

    for i in range(qn):
        switch = 0
        a = [idx, i]
        lst[idx] = i
        if idx == 0:
            queen(lst, qn, idx + 1)
        else:
            for j in range(idx):
                if abs(j - a[0]) == abs(lst[j] - a[1]) or lst[j] == a[1]:
                    switch = 1
                    break

            if switch == 0:
                queen(lst, qn, idx + 1)
        lst[idx] = -1
        switch = 0


n = int(sys.stdin.readline())
answer = 0
board = [-1] * n

queen(board, n, 0)

print(answer)
