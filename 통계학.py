import sys
n = int(sys.stdin.readline())
lst = [int(sys.stdin.readline()) for _ in range(n)]
lst.sort()
# 산술평균
print(round(sum(lst)/n))
# 중앙값
print(lst[(n//2)])
# 최빈값


x = min(lst)

if x < 0:
    x = abs(x)
    tmp = [0] * (max(lst) + x+1)

    for i in lst:
        tmp[i+x] += 1
    maxx = 0
    for i in tmp:
        if i > maxx:
            maxx = i
    c = 0
    for i in tmp:
        if maxx == i:
            c += 1
    if c >= 2:
        count = 0
        for i in range(len(tmp)):
            if tmp[i] == max(tmp):
                count += 1
                if count == 2:
                    print(i-x)
                    break
    else:
        print(tmp.index(max(tmp))-x)

else:
    tmp = [0] * (max(lst)+1)
    for i in lst:
        tmp[i] += 1
    maxx = 0
    for i in tmp:
        if i > maxx:
            maxx = i
    c = 0
    for i in tmp:
        if i == maxx:
            c += 1
    if c >= 2:
        count = 0
        for i in range(len(tmp)):
            if tmp[i] == max(tmp):
                count += 1
                if count == 2:
                    print(i)
                    break
    else:
        print(tmp.index(max(tmp)))


# 범위
print(max(lst) - min(lst))
