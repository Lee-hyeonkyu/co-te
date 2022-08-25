def solution(n, lost, reserve):
    a = set(lost) - set(reserve)
    b = set(reserve) - set(lost)

    for i in b:
        if i-1 in a:
            a.remove(i-1)
        elif i+1 in a:
            a.remove(i+1)

    return n - len(a)
