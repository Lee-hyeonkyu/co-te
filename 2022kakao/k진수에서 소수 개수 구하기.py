n = 110011
k = 10


def solution(n, k):
    answer = 0
    tmp = ''
    while n != 0:
        tmp = str(n % k) + tmp
        n //= k

    tmp = tmp.split('0')
    for i in tmp:
        if len(i) and int(i) >= 2:
            s = True
            for j in range(2, int(int(i)**.5) + 1):
                if int(i) % j == 0:
                    s = False
                    break
            if s:
                answer += 1

    return answer


print(solution(n, k))
