citations = [9, 9, 9, 9, 9, 9]


def solution(citations):
    citations.sort(reverse=True)
    for a, b in enumerate(citations):
        print(a, b)
        if a >= b:
            return a
    return len(citations)


print(solution(citations))
