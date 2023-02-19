n = 6
times = [7, 10]


def solution(n, times):
    answer = 0
    left = min(times)
    right = max(times)*n
    while left <= right:
        mid = (left + right) // 2
        checked = 0
        for time in times:
            checked += mid // time
        if checked >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer


print(solution(n, times))


# =============================


n, m = map(int, input().split())
lst = [int(input()) for _ in range(n)]

start = 0
end = 1_000_000_000_000_000_000


while start+1 < end:
    center = (start+end)//2
    tmp = 0
    for i in lst:
        tmp += center // i

    if tmp >= m:
        end = center
    else:
        start = center

print(end)
