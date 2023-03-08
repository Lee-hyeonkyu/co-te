import heapq
n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
lst.sort()
tmp = []
print(lst)
heapq.heappush(tmp, lst[0][1])
for i in range(1, n):
    print("lst: ", lst[i], "tmp: ", tmp[0])
    if lst[i][0] < tmp[0]:
        heapq.heappush(tmp, lst[i][1])
    else:
        heapq.heappop(tmp)
        heapq.heappush(tmp, lst[i][1])
    print(tmp)

print(len(tmp))
