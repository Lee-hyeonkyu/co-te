park = ["SOO", "OOO", "OOO"]
routes = ["E 2", "S 2", "W 1"]

loc = {"N": [-1, 0], "E": [0, 1], "W": [0, -1], "S": [1, 0]}


def check(dir, l, park, x, y):
    if l == 0:
        return True
    dx, dy = loc[dir]
    if (
        0 <= (dx + x) < len(park)
        and 0 <= (dy + y) < len(park[0])
        and park[dx + x][dy + y] != "X"
    ):
        return check(dir, l - 1, park, dx + x, dy + y)
    else:
        return False


def solution(park, routes):
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == "S":
                x, y = i, j
    for i in routes:
        dir, l = i.split()
        l = int(l)
        if check(dir, l, park, x, y):
            dx, dy = loc[dir]
            dx *= l
            dy *= l
            x += dx
            y += dy

    return [x, y]


print(solution(park, routes))
