import math

n = int(input())
room = list(map(int, input().split()))
spvr = list(map(int, input().split()))

cnt = 0
for i in range(n):
    x = room[i]-spvr[0]
    if x <= 0:
        pass
    elif x <= spvr[1]:
        cnt += 1
    else:
        cnt += math.ceil(x/spvr[1])
print(cnt+n)
