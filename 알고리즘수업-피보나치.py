n = int(input())

d = [0] * 41


def fib(n):
    if n <= 2:
        return 1

    if not d[n]:
        d[n] = fib(n-1) + fib(n-2)

    return d[n]


print(fib(n), n-2)
