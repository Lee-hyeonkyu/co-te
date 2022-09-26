
today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]


def check(m, p, today):

    t_y, t_m, t_d = today.split(".")
    n, y = 0, 0
    year, month, day = p.split(".")
    r = day[-1]
    day = int(day[:2]) - 1

    if day == 0:
        day = 28
        month = int(month) - 1
        if month == 0:
            month = 12
            year = int(year) - 1

    if m > 12:
        n = m % 12
        y = m//12
    elif m == 12:
        y = 1
    else:
        n = m
    month = int(month) + n

    if month > 12:
        month -= 12
        y += 1
    year = int(year) + y

    print(year, month, day)
    if int(t_y) > year:
        return 1
    elif int(t_y) == year:
        if int(t_m) > month:
            return 1
        elif int(t_m) == month:
            if int(t_d) > day:
                return 1
            else:
                return 0
        else:
            return 0
    else:
        return 0


def solution(today, terms, privacies):
    pri = []
    answer = []
    for p in privacies:
        for i in range(len(terms)):
            if terms[i][0] in p:
                pri.append(check(int(terms[i][1:]), p, today))
    for i in range(len(pri)):
        if pri[i]:
            answer.append(i+1)

    return answer
