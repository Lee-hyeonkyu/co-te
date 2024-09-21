n, m = map(int, input().split())

seq = list(map(int, input().split()))

seq.sort()


def permutations(n, m):
    def backtrack(lst):
        if len(lst) == m:
            print(" ".join(map(str, lst)))
            return
        for i in seq:
            if i not in lst:
                lst.append(i)
                backtrack(lst)
                lst.pop()

    backtrack([])


permutations(n, m)
