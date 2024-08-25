# n = int(input())

# c_paper = [list(map(int, input().split())) for _ in range(n)]


# # for i in c_paper:
# #     print(i)


# cnt = 0


# white = 0
# blue = 0
# lst = [0] * 4

# def check(k):
#     global white, blue
#     x = n // k  # 2
#     for i in range(x):
#         print()
#         left = 0
#         right = 0
#         for j in range(k):
#             print(c_paper[k * i + j])
#             for w in range(n):
#                 if w < 4:
#                     left += c_paper[k * i + j][w]
#                 else:
#                     right += c_paper[k * i + j][w]
#         if left == k**2 or left == 0:
#             lst[i * 2 + 0] = 1
#             if left == 0:
#                 white += 1
#             else:
#                 blue += 1

#         if right == k**2 or right == 0:
#             lst[i * 2 + 1] = 1
#             if right == 0:
#                 white += 1
#             else:
#                 blue += 1

#         print(left, right, i)


# for i in range(n):
#     if sum(c_paper[i]) != 8:
#         check(n // 2)
#         break

# print(blue, white)
# print(lst)


n = int(input())
c_paper = [list(map(int, input().split())) for _ in range(n)]

white = 0
blue = 0


def check(x, y, size):
    global white, blue
    initial_color = c_paper[x][y]
    all_same = True

    for i in range(x, x + size):
        for j in range(y, y + size):
            if c_paper[i][j] != initial_color:
                all_same = False
                break
        if not all_same:
            break

    if all_same:
        if initial_color == 0:
            white += 1
        else:
            blue += 1
    else:
        new_size = size // 2
        check(x, y, new_size)
        check(x, y + new_size, new_size)
        check(x + new_size, y, new_size)
        check(x + new_size, y + new_size, new_size)


check(0, 0, n)
print(white)
print(blue)
