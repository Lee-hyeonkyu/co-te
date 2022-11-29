def whiing(go, i, map):
    global pox, poy, answer

    for _ in range(go):
        pox += dx[i]
        poy += dy[i]
        # print('------:', pox, poy)
        if poy < 0:
            break

        whii = 0

        for x, y, z in map:
            new_pos_x = pox + x
            new_pos_y = poy + y

            if z == 0:
                morae = board[pox][poy] - whii
            else:
                morae = int(board[pox][poy] * z)
                whii += morae

            if 0 <= new_pos_x < n and 0 <= new_pos_y < n:
                board[new_pos_x][new_pos_y] += morae
            else:
                answer += morae


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]


l = [[-2, 0, .02], [2, 0, .02], [-1, -1, .1], [-1, 0, .07], [-1, 1, .01],
     [1, -1, .1], [1, 0, .07], [1, 1, .01], [0, -2, .05], [0, -1, 0]]
d = [[0, -2, .02], [0, 2, .02], [1, -1, .1], [0, -1, .07], [-1, -1, .01],
     [1, 1, .1], [0, 1, .07], [-1, 1, .01], [2, 0, .05], [1, 0, 0]]
r = [[-2, 0, .02], [2, 0, .02], [-1, -1, .01], [-1, 0, .07], [-1, 1, .1],
     [1, -1, .01], [1, 0, .07], [1, 1, .1], [0, 2, .05], [0, 1, 0]]
u = [[0, -2, .02], [0, 2, .02], [-1, -1, .1], [0, -1, .07], [1, -1, .01],
     [-1, 1, .1], [0, 1, .07], [1, 1, .01], [-2, 0, .05], [-1, 0, 0]]


dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

pox = n//2
poy = n//2
answer = 0


for i in range(1, n+1):
    if i % 2:
        whiing(i, 0, l)
        whiing(i, 1, d)
    else:
        whiing(i, 2, r)
        whiing(i, 3, u)

print(answer)
