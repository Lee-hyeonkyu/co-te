d = [0] * 101

d[1] = 1
d[2] = 1
d[3] = 1
d[4] = 2


def wave(n):
    for i in range(5, n+1):
        if not d[i]:
            d[i] = d[i-2] + d[i-3]

    return d[n]


for _ in range(int(input())):
    print(wave(int(input())))
