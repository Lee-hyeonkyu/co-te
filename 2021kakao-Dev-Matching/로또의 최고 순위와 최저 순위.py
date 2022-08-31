def check(num):
    if 7 - num >= 6:
        return 6
    else:
        return 7 - num


def solution(lottos, win_nums):
    cnt = 0
    zero = 0

    # 0의 갯수
    for i in lottos:
        if i == 0:
            zero += 1
    # 맞는 숫자
    for i in lottos:
        if i in win_nums:
            cnt += 1

    mini = cnt
    maxi = cnt + zero
    answer = [check(maxi), check(mini)]
    return answer
