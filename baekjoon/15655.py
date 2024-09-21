n, m = map(int, input().split())

seq = list(map(int, input().split()))

seq.sort()


def permutation(n, m):
    def backtracking(lst):
        if len(lst) == m:
            print(" ".join(map(str, lst)))
            return
        for i in seq:
            if not len(lst) or (len(lst) >= 1 and lst[-1] < i):
                lst.append(i)
                backtracking(lst)
                lst.pop()

    backtracking([])


permutation(n, m)
