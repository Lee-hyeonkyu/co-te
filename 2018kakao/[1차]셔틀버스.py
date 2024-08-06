def two_word(word):
    if len(str(word)) == 1:
        return "0" + str(word)
    else:
        return str(word)


def convert_int(strtime):
    hour = strtime[:2]
    minute = strtime[-2:]

    return 60 * int(hour) + int(minute)


def convert_str(inttime):
    hour = inttime // 60
    minute = inttime % 60
    return two_word(hour) + ":" + two_word(minute)


def solution(n, t, m, timetable):
    answer = None
    people = []
    bus_table = [540]
    for person in timetable:
        people.append(convert_int(person))
    people.sort()
    for i in range(n - 1):
        bus_table.append(bus_table[i] + t)

    people_get = 0

    for i in range(1, n + 1):
        mx = 0
        rest_people = people[people_get:]

        for j in range(len(rest_people)):
            if bus_table[i - 1] >= rest_people[j]:
                people_get += 1
                mx += 1
            if mx == m:
                if i == n:
                    answer = rest_people[j] - 1
                break

    if answer == None:
        answer = bus_table[i - 1]

    answer = convert_str(answer)
    return answer
