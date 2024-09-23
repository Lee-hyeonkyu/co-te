import copy

board = [list(map(int, input().split())) for _ in range(int(input()))]
answer = 0
dir = {0: "up", 1: "down", 2: "left", 3: "right"}


def move(lst):
    non_zero = [x for x in lst if x != 0]
    new_lst = []
    i = 0
    while i < len(non_zero):
        if i < len(non_zero) - 1 and non_zero[i] == non_zero[i + 1]:
            new_lst.append(non_zero[i] * 2)
            i += 2
        else:
            new_lst.append(non_zero[i])
            i += 1
    new_lst += [0] * (len(lst) - len(new_lst))
    return new_lst


def transpose(board):
    return [list(row) for row in zip(*board)]


def move_board(board, dir):
    if dir == "left":
        return [move(row) for row in board]
    if dir == "right":
        return [move(row[::-1])[::-1] for row in board]
    if dir == "up":
        moved = [move(row) for row in transpose(board)]
        return transpose(moved)
    else:
        moved = [move(row[::-1])[::-1] for row in transpose(board)]
        return transpose(moved)


def bt(lst):
    global answer
    if len(lst) == 5:
        board_ = copy.deepcopy(board)
        for i in lst:
            board_ = move_board(board_, dir[i])
        for row in board_:
            answer = max(answer, max(row))
        return
    for i in range(4):
        lst.append(i)
        bt(lst)
        lst.pop()


bt([])
print(answer)
