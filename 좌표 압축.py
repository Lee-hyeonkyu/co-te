import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
s_lst = sorted(set(lst))
answer = {s_lst[i]: i for i in range(len(s_lst))}
print(" ".join(map(str, [answer[i] for i in lst])))
