a, b, c, d, e, f = map(int, input().split())

print(
    *[
        [i, j]
        for i in range(-999, 1000)
        for j in range(-999, 1000)
        if (a * i) + (b * j) == c and (d * i) + (e * j) == f
    ][0]
)


# for i in range(-999, 1000):
#     for j in range(-999, 1000):
#         if (a * i) + (b * j) == c and (d * i) + (e * j) == f:
#             print(i, j)
