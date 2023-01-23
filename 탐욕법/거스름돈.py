cnt = 0
type = [500, 100, 50, 10, 5, 1]
change = 1000 - int(input())

for t in type:
    cnt += change // t
    change %= t

# # while change:
# #     if change >= 500:
# #         cnt += 1
# #         change -= 500
# #     elif change >= 100:
# #         cnt += 1
# #         change -= 100
# #     elif change >= 50:
# #         cnt += 1
# #         change -= 50
# #     elif change >= 10:
# #         cnt += 1
# #         change -= 10
# #     elif change >= 5:
# #         cnt += 1
# #         change -= 5
# #     else:
# #         cnt += 1
# #         change -= 1

print(cnt)
