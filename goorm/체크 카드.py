from collections import deque

bank, n = map(int, input().split())
bank_lst = deque([list(input().split(" ")) for _ in range(n)])
processing = deque()
cnt = 0

# 실패 13,14,15 : reservation은 승인 불가하면 deposit될 때 마다 확인 후 금액 차감.
# while cnt != n:
#     cnt += 1
#     task = bank_lst.popleft()
#     if task[0] == 'deposit':
#         bank += int(task[1])
#     elif task[0] == 'pay':
#         if bank >= int(task[1]):
#             bank -= int(task[1])
#     elif task[0] == 'reservation':
#         if not processing:
#             if bank >= int(task[1]):
#                 bank -= int(task[1])
#             else:
#                 processing.append(task)
#                 bank_lst.append(task)
#                 cnt -= 1
#         else:
#             if task != processing[0]:
#                 processing.append(task)
#                 bank_lst.append(task)
#                 cnt -= 1
#             else:
#                 processing.popleft()
#                 if bank >= int(task[1]):
#                     bank -= int(task[1])

# print(bank)


for task in bank_lst:
    if task[0] == 'deposit':
        bank += int(task[1])
        while processing:
            if processing[0] > bank:
                break
            else:
                bank -= processing[0]
                processing.popleft()

    elif task[0] == 'pay':
        if bank >= int(task[1]):
            bank -= int(task[1])
    elif task[0] == 'reservation':
        if not processing:
            if bank >= int(task[1]):
                bank -= int(task[1])
            else:
                processing.append(int(task[1]))
        else:
            processing.append(int(task[1]))
print(bank)
