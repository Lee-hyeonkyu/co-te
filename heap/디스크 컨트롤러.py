import heapq

jobs = [[0, 3], [1, 9], [2, 6]]


jobs = sorted(jobs)

now = 0  # 진행상황
time = 0  # 총시간
lst = []  # 힙구조 리스트

for i in jobs:
    heapq.heappush(lst, i[::-1])  # 앞뒤 순서 바꿔서 힙구조 사용
