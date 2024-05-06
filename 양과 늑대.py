# from collections import deque

# info = [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1]
# edges = [
#     [0, 1],
#     [1, 2],
#     [1, 4],
#     [0, 8],
#     [8, 7],
#     [9, 10],
#     [9, 11],
#     [4, 3],
#     [6, 5],
#     [4, 6],
#     [8, 9],
# ]


# def check(num):
#     for s, e in edges:
#         if num == s:
#             return True
#     return False


# idx = 0

# while 1:
#     if idx >= len(edges):
#         break
#     tmp = edges[idx]

#     if not check(tmp[1]):
#         if info[tmp[1]]:
#             del edges[idx]
#             idx -= 1
#     idx += 1

# shp_wlf = [1, 0]
# start = 0

# for i in edges:
#     if start == i[0]:
#         if info[i[1]]:
#             if shp_wlf[1] + 1 < shp_wlf[0]:
#                 shp_wlf[1] += 1
#             else:
#                 break
#         else:
#             shp_wlf[0] += 1


info = [0, 0, 1, 0, 1]
edges = [[0, 1], [1, 2], [1, 4], [4, 3]]
visited = [0] * len(info)
visited[0] = 1
answer = []


def recursive(sheep, wolf):
    if sheep > wolf:
        answer.append(sheep)
    else:
        return None

    for s, e in edges:
        if visited[s] and not visited[e]:
            visited[e] = 1
            if not info[e]:
                recursive(sheep + 1, wolf)
            else:
                recursive(sheep, wolf + 1)
            visited[e] = 0


recursive(1, 0)
print(max(answer))
