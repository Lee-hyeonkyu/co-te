k, n = map(int, input().split())
lan = [int(input()) for _ in range(k)]


def parametric_search(lan, n):
    left, right = 1, max(lan)
    best = 1
    cut_cnt = 0
    while left <= right or cut_cnt < n:
        mid = (left + right) // 2
        cut_cnt = sum(i // mid for i in lan)
        if cut_cnt >= n:
            left = mid + 1
            best = mid
        elif cut_cnt < n:
            right = mid - 1

    return best


print(parametric_search(lan, n))


# k, n = map(int, input().split())
# lan = [int(input()) for _ in range(k)]


# def parametric_search(lan, n):
#     left, right = 1, sum(lan) // n
#     while left <= right:
#         mid = (left + right) // 2
#         cut_cnt = sum(i // mid for i in lan)
#         if cut_cnt >= n:
#             left = mid + 1
#         else:
#             right = mid - 1

#     return right


# print(parametric_search(lan, n))
