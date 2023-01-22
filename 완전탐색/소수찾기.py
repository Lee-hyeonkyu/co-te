from itertools import permutations

# 소수찾기


# def prime(num):
#     if num == 0 or num == 1:
#         return False
#     elif num == 2:
#         return True
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True


# def solution(numbers):
#     cnt = 0
#     all = []
#     # 순열
#     for i in range(1, len(numbers) + 1):
#         temp = list(permutations(numbers, i))
#         all += [int("".join(i)) for i in temp]
#     # 중복 제거
#     all = set(all)
#     for i in all:
#         if prime(i):
#             cnt += 1
#     return cnt


numbers = '17'


def check_prime(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def solution(numbers):
    answer = []
    cnt = 0
    for i in range(1, len(numbers) + 1):
        tmp = list(permutations(numbers, i))
        answer += [int("".join(i)) for i in tmp]

    answer = set(answer)

    for i in answer:
        if check_prime(i):
            cnt += 1

    return cnt


print(solution(numbers))
