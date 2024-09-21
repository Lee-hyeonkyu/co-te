n, m = map(int, input().split())

seq = sorted(list(map(int, input().split())))


def p(n, m):
    def bt(lst):
        if len(lst) == m:
            print(" ".join(map(str, lst)))
            return
        for i in seq:
            lst.append(i)
            bt(lst)
            lst.pop()

    bt([])


p(n, m)
