import heapq

operations = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]


def solution(operations):
    x = []

    for i in operations:
        if "I" in i:
            heapq.heappush(x, int(i[1:]))
        else:
            if int(i[1:]) == 1:
                if len(x) != 0:
                    x.pop(x.index(int(heapq.nlargest(1, x)[0])))
            else:
                heapq.heappop(x)
    if len(x) == 0:
        return [0, 0]
    return [max(x), min(x)]


print(solution(operations))


t = [8, 3, 4, 1, 2]
# z = []
# for i in t:
#     heapq.heappush(z,i)
# print(z)

# print(z.pop(z.index(int(heapq.nlargest(1,z)[0]))))
