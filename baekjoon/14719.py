h, w = map(int, input().split())

blocks = list(map(int, input().split()))

board = [[0] * w for _ in range(h)]


for i in range(len(blocks)):
    for b in range(1, blocks[i] + 1):
        board[-b][i] = 1

cnt = 0

for line in board:
    start, switch = 0, 0
    for i in range(len(line)):
        if line[i]:
            if not switch:
                switch = 1
                start = i
            else:
                cnt += line[start:i].count(0)
                start = i

print(cnt)


H, W = map(int, input().split())
ground = list(map(int, input().split()))

result = 0
for i in range(1, W - 1):
    left_max = max(ground[:i])
    right_max = max(ground[i + 1 :])

    compare = min(left_max, right_max)

    if ground[i] < compare:
        result += compare - ground[i]

print(result)

# [4,0,2,3]
"""

1 0 0 0
1 0 0 1
1 0 1 1
1 0 1 1

"""
