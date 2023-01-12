from collections import defaultdict
import pprint

info = [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1]
edges = [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [
    9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]

tree = defaultdict(list)

for s, e in edges:
    tree[s].append(e)


pprint.pprint(tree)


print(tree[4])


# def solution(info, edges):
#     answer = 0
#     return answer
