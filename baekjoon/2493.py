import sys

input = sys.stdin.readline

n = int(input())

lst = list(map(int, input().split()))
answer = [0]

for i in range(1, n):
    tmp = i - 1
    while 1:
        if lst[tmp] < lst[i]:
            if answer[tmp] == 0:
                answer.append(0)
                break
            else:
                tmp = answer[tmp] - 1
        else:
            answer.append(tmp + 1)
            break

print(" ".join(map(str, answer)))
