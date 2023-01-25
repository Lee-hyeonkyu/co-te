n = int(input())

lst = list(map(int, input().split()))

cont_l = 0
re_l = 0
cont_r = 0
re_r = 0


for i in range(n):
    if n == 1:
        break
    if lst[i] == 1:
        cont_l += 1
    else:
        re_l = max(re_l, cont_l)
        cont_l = 0

for i in range(n):
    if n == 1:
        break
    if lst[i] == 2:
        cont_r += 1
    else:
        re_r = max(re_r, cont_r)
        cont_r = 0


if re_l == 1:
    re_l = 0
if re_r == 1:
    re_r = 0

if not abs(re_l - re_r):
    print(1)
else:
    print(abs(re_l - re_r))
