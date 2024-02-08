p, m = map(int, input().split())
l, n = input().split()
room = []
room.append([[int(l), n]])
for _ in range(p - 1):
    l, n = input().split()
    getin = False
    for r in room:
        if len(r) < m and abs(r[0][0] - int(l)) <= 10:
            r.append([int(l), n])
            getin = True
            break
    if not getin:
        room.append([[int(l), n]])


for r in room:
    r = sorted(r, key=lambda x: x[1])

    if len(r) == m:
        print("Started!")
        for i, j in r:
            print(i, j)
    else:
        print("Waiting!")
        for i, j in r:
            print(i, j)
