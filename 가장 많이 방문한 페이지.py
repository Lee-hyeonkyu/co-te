s = "1 2 3 4 B B 42 B F F"


def solution(s):
    answer = 0
    page_log = []
    back_log = []
    page_dict = dict()

    for i in s.split():
        if i == "B":
            if len(page_log) > 1:
                back_log.append(page_log.pop())
        elif i == "F":
            if back_log:
                page_log.append(back_log.pop())
        else:
            page_log.append(i)
            back_log = list()

        if not page_log:
            continue
        elif page_log[-1] in page_dict:
            page_dict[page_log[-1]] += 1
        else:
            page_dict[page_log[-1]] = 1

    answer = max(page_dict.values())

    return answer


print(solution(s))
