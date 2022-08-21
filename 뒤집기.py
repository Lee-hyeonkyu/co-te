import math
n = str(input())
start = n[0]
lst = []
cnt = 0

for i in range(len(n)):
    if n[i] != start:
        start = n[i]
        cnt +=1
print( math.ceil(cnt/2))

