from itertools import combinations
from collections import Counter

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2, 3, 4]


def solution(orders, course):
    answer = []

    for c in course:
        tmp = []
        for o in orders:
            tmp += combinations(sorted(o), c)
        x = Counter(tmp)
        if len(x) > 0:
            m = max(list(x.values()))
            if m >= 2:
                for k, v in x.items():
                    if v == m:
                        answer.append("".join(k))

    return sorted(answer)


print(solution(orders, course))
