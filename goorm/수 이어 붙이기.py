# import itertools

# n = int(input())
# m = list(input().split())

# m = sorted(m)


# x = list(itertools.permutations(m, n))

# lst = []

# for i in range(len(x)):
#     tmp = ''
#     num = ''.join(x[i])
#     for j in range(len(num)):
#         if tmp == num[j]:
#             lst.append(int(num[0:j]+num[j+1:]))
#             break
#         else:
#             tmp = num[j]
#     if len(lst) != int(i+1):
#         lst.append(int(num))

# print(min(lst))
