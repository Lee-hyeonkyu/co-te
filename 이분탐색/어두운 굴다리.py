import math

n = int(input())
m = int(input())
lst = list(map(int, input().split()))

answer = lst[0]

for i in range(1, m):
    answer = max(math.ceil((lst[i]-lst[i-1])/2), answer)
answer = max(answer, n - lst[m-1])
print(answer)


