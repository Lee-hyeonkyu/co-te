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
