play_time = '02:03:55'
adv_time = '00:14:15'
logs = ["01:20:15-01:45:14", "00:40:31-01:00:00",
        "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]


def str_toint(time):
    hours, minutes, seconds = time.split(":")
    return 3600*int(hours) + 60*int(minutes)+int(seconds)


def int_tostr(time):
    hours = "0"+str(time//3600)
    minutes = "0"+str((time % 3600) // 60)
    seconds = "0"+str((time % 3600) % 60)
    return ":".join([hours[-2:], minutes[-2:], seconds[-2:]])


def solution(play_time, adv_time, logs):

    max_time = 0
    pltam = str_toint(play_time)
    adtam = str_toint(adv_time)
    time = [0 for _ in range(pltam+1)]

    for i in logs:
        start, end = i.split("-")
        start, end = str_toint(start), str_toint(end)
        time[start] += 1
        time[end] -= 1

    for i in range(1, len(time)):
        time[i] += time[i-1]
    for i in range(1, len(time)):
        time[i] += time[i-1]

    view = time[adtam-1]

    for i in range(adtam-1, pltam):
        ttime = time[i]-time[i-adtam]
        if view < ttime:
            view = ttime
            max_time = i + 1 - adtam

    return int_tostr(max_time)


print(solution(play_time, adv_time, logs))
