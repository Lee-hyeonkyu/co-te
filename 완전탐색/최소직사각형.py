sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]


def solution(sizes):
    a = 0
    b = 0
    for i in sizes:
        a = max(max(i), a)
        b = max(min(i), b)
    return a*b


print(solution(sizes))
