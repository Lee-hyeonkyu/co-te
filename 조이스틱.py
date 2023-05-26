name = "JEROEN"


def check(name_):
    sub = ["A"] * len(name_)
    name_ = list(name_)
    cnt = -1

    for i in range(len(name_)):
        if sub == name_:
            break
        cnt += min(ord(name_[i]) - 65, 91 - ord(name_[i]))
        cnt += 1
        sub[i] = name_[i]
    return cnt


def solution(name):
    answer = min(check(name), check(name[0] + name[::-1][:-1]))
    for i in range(len(name)):
        answer = min(
            answer,
            min(
                check(name[: i + 1][::-1] + name[i + 1 :][::-1]) + i,
                check(name[-i:] + name[:-i]) + i,
            ),
        )
    if answer == -1:
        return 0
    return answer
