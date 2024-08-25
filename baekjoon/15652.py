n, m = map(int, input().split())


def permutation(n, m):
    def backtracking(lst):
        if len(lst) == m:
            print(" ".join(map(str, lst)))
            return

        for i in range(1, n + 1):
            if (len(lst) != 0 and lst[-1] <= i) or not len(lst):
                lst.append(i)
                backtracking(lst)
                lst.pop()

    backtracking([])


permutation(n, m)
