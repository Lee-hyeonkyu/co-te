# from collections import deque
from collections import defaultdict


tickets = [["ICN", "SFO"], ["ICN", "ATL"], [
    "SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]

# test 1,2 시간초과

# def solution(tickets):
#     answer = []
#     lst = deque()
#     tickets = sorted(tickets, key=lambda x: x[1])
#     for i in tickets:
#         lst.append(i)

#     start = 'ICN'
#     x = []
#     now = start
#     while lst:
#         p = lst.popleft()
#         if p[0] == now:
#             answer.append(now)
#             now = p[1]
#         else:
#             lst.append(p)
#     answer.append(now)
#     return answer


# print(solution(tickets))

def solution(tickets):
    answer = []
    tickets = sorted(tickets, key=lambda x: x[1], reverse=True)
    dd = defaultdict(list)
    for i, j in tickets:
        dd[i].append(j)

    start = ["ICN"]
    print(dd)
    while start:
        x = start[-1]

        if x not in dd or not dd[x]:
            answer.append(start.pop())
        else:
            start.append(dd[x][-1])
            dd[x] = dd[x][:-1]
    return answer[::-1]


print(solution(tickets))
