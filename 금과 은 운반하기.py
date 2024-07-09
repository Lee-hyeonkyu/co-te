a = 10
b = 10
g = [100]
s = [100]
w = [7]
t = [10]


# def check(mid, a, b, g, s, w, t):
#     gold, silver, weight = 0, 0, 0

#     for i in range(len(g)):
#         cnt = mid // (t[i] * 2)

#         if mid % (t[i] * 2) >= t[i]:
#             cnt += 1

#         tmp = min(cnt * w[i], g[i] + s[i])
#         weight += tmp
#         gold += min(tmp, g[i])
#         silver += min(tmp, s[i])

#     if weight >= a + b and gold >= a and silver >= b:
#         return True
#     return False


# def solution(a, b, g, s, w, t):
#     left = 0
#     right = 1000000000000000
#     while left + 1 < right:
#         mid = (left + right) // 2
#         if check(mid, a, b, g, s, w, t):
#             right = mid
#         else:
#             left = mid
#     return right


def solution(a, b, g, s, w, t):
    left, right = 0, 10e15
    while left < right:
        mid = (left + right) // 2
        gold, silver, total = 0, 0, 0

        for i in range(len(g)):
            tmp = mid // t[i]
            cnt = tmp // 2 + tmp % 2
            gold += min(g[i], w[i] * cnt)
            silver += min(s[i], w[i] * cnt)
            total += min(g[i] + s[i], w[i] * cnt)
            # print(cnt, gold, silver, total)
            # print(left, mid, right, cnt)

        if gold < a or silver < b or total < a + b:
            left = mid + 1
        else:
            right = mid

    return right


print(solution(a, b, g, s, w, t))
