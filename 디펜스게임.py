import heapq as q

n = 7
k = 3

enemy = [4, 2, 4, 5, 3, 3, 1]


# 몇몇 시간 초과

# def solution(n, k, enemy):
#     lst = []
#     for i in range(len(enemy)):
#         lst.append(enemy[i])
#         if len(lst) > k:
#             lst.sort()
#             n -= lst.pop(0)
#         if n < 0:
#             return i
#     return len(enemy)


# print(solution(n, k, enemy))


def solution(n, k, enemy):
    lst = []
    for i in range(len(enemy)):
        q.heappush(lst, enemy[i])
        if len(lst) > k:
            n -= q.heappop(lst)
        if n < 0:
            return i
    return len(enemy)


print(solution(n, k, enemy))
