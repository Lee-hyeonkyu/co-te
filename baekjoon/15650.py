n, m = map(int, input().split())


def permutations(n, m):
    def backtrack(lst):
        if len(lst) == m and sorted(lst) == lst:
            print(" ".join(map(str, lst)))
            return

        for i in range(1, n + 1):
            if i not in lst:
                lst.append(i)
                backtrack(lst)
                lst.pop()

    backtrack([])


permutations(n, m)
