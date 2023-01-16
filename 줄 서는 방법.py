n = 3
k = 5


def factorial(number):
    if number <= 1:
        return 1
    else:
        return number * factorial(number-1)


def solution(n, k):
    lst = [i for i in range(1, n+1)]
    answer = []
    k -= 1

    while lst:
        a = k // factorial(n-1)
        k %= factorial(n-1)
        answer.append(lst.pop(a))
        n -= 1

    return answer


print(solution(n, k))
