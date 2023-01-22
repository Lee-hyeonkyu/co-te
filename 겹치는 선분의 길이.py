lines = [[0, 2], [-3, -1], [-2, 1]]
# lines = [[0, 1], [2, 5], [3, 9]]


# def solution(lines):
#     answer = 0
#     start = 0
#     end = 0
#     lines.sort()
#     for a, b in lines:
#         start = min(start, a)
#         end = abs(max(end, b))

#     if start < 0:
#         start = -start
#         end += start
#     else:
#         start -= start
#         end -= start
#     lst = [0] * (end+1)
#     for line in lines:
#         for i in range(line[0]+start, line[1]+start+1):
#             lst[i] += 1

def solution(lines):
    lst = [0]*200

    for i in range(3):
        for j in range(lines[i][0]+100, lines[i][1]+100):
            lst[j] += 1
    print(lst)
    return 0


print(solution(lines))
