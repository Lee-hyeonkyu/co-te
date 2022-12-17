k = [input() for _ in range(5)]

for i in k:
    a = 0
    tmp = 1
    for j in range(7):
        if not j % 2:
            a += int(i[j])
        elif int(i[j]):
            tmp *= int(i[j])
    a *= tmp
    print(a % 10)
