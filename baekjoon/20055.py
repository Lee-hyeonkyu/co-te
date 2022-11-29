n, k = map(int, input().split())

belt = list(map(int, input().split()))


def solution(n, k, belt):
    rb = [0] * n
    answer = 0

    while 1:
        answer += 1
        belt = [belt[-1]] + belt[:-1]
        rb = [rb[-1]] + rb[:-1]
        rb[n-1] = 0

        for i in range(n-2, -1, -1):
            if rb[i] and rb[i+1] == 0 and belt[i+1]:
                belt[i+1] -= 1
                rb[i] = 0
                rb[i+1] = 1

        rb[n-1] = 0
        if belt[0] and rb[0] == 0:
            belt[0] -= 1
            rb[0] = 1

        cnt = belt.count(0)
        if cnt >= k:
            break

    return answer


print(solution(n, k, belt))
