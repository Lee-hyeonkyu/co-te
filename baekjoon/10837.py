"""
영희가 높을 때  -> 영희 - 동수 - 남은 라운드 <= 2 까지 가능 
동수가 높을 때 -> 영희 - 동수 + 남은 라운드 >= -1 까지 가능
"""

import sys

k = int(sys.stdin.readline())
lst = []
for _ in range(int(sys.stdin.readline())):
    m, n = map(int, sys.stdin.readline().split())
    if m > n:
        r = k - m
        if m - n - r <= 2:
            lst.append(1)
        else:
            lst.append(0)
    elif m < n:
        r = k - n
        if m - n + r >= -1:
            lst.append(1)
        else:
            lst.append(0)
    else:
        lst.append(1)

for i in lst:
    print(i)
"""
5
4
5 5
5 1
0 3
1 4

"""
