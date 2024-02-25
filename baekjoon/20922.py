N, K = map(int, input().split())

lst = list(map(int, input().split()))

start, end = 0, 0
cnt_lst = [0] * (max(lst) + 1)

answer = 0

while end != N:
    if cnt_lst[lst[end]] < K:
        cnt_lst[lst[end]] += 1
        end += 1
    else:
        cnt_lst[lst[start]] -= 1
        start += 1
    answer = max(answer, end - start)
print(answer)


# while end != N - 1:
#     dct[lst[end]] += 1
#     while max(dct.values()) > K:
#         dct[start] -= 1
#         start += 1
#     answer = max(answer, end - start)
#     end += 1
