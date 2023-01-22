from collections import defaultdict

survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]


def solution(survey, choices):
    answer = ''
    check_lst = ["RT", "CF", "JM", "AN"]
    length = len(survey)
    result_lst = defaultdict(int)

    for i in range(length):
        s = survey[i]
        c = choices[i]
        if c - 4 > 0:
            result_lst[s[1]] += c-4
        elif c - 4 < 0:
            result_lst[s[0]] += abs(c-4)
    for i in check_lst:
        a = 0
        b = 0
        for j in result_lst:
            if j in i:
                if j == i[0]:
                    a += result_lst[j]
                else:
                    b += result_lst[j]
        if a >= b:
            answer += i[0]
        else:
            answer += i[1]
    return answer


print(solution(survey, choices))
