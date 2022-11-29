import time

s_time = time.time()
n, m, k = 5, 8, 3
lst = [2, 4, 5, 4, 6]


def solution(n, m, k, lst):
    answer = 0
    lst.sort()
    first = lst[n-1]
    second = lst[n-2]

    while 1:
        for i in range(k):
            if m == 0:
                break
            answer += first
            m -= 1
        if m == 0:
            break
        answer += second
        m -= 1

    return answer


solution(n, m, k, lst)

e_time = time.time()

print("1번 풀이 시간:", e_time - s_time)


s_1time = time.time()


def solution_2(n, m, k, lst):
    answer = 0
    lst.sort()
    first = lst[n-1]
    second = lst[n-2]

    cnt = int(m/(k+1)) * k
    cnt += m % (k+1)

    answer += cnt * first
    answer += (m - cnt) * second

    return answer


solution_2(n, m, k, lst)

e_1time = time.time()

print('2번 풀이 시간:', e_1time - s_1time)
