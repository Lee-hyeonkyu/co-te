from datetime import datetime, timedelta

def solution(book_time):
    book_time.sort()
    lst = []
    lst.append(book_time[0][1])
    answer = 1
    time_format = "%H:%M"
    for i in range(1,len(book_time)):
        lst.sort()
        checkin_time = datetime.strptime(book_time[i][0],time_format)
        plus = False
        for j in range(len(lst)):
            checkout_time = datetime.strptime(lst[j],time_format) + timedelta(minutes=10)
            if not plus and checkin_time >= checkout_time:
                lst[j] = book_time[i][1]
                plus = True
        if not plus:
            lst.append(book_time[i][1])
            answer += 1

    return answer


################### 누적합

def c_s(arr):
    lst = [0 for _ in range(len(arr)+1)]
    for i in range(len(arr)):
        lst[i+1] = lst[i] + arr[i]
    return lst

def solution(book_time):
    ck_time = [0 for _ in range(24*60)]
    for ckin,ckout in book_time:
        ckin = int(ckin[:2]) * 60 + int(ckin[3:])
        ckout = int(ckout[:2]) * 60 + int(ckout[3:]) + 10
        if ckout > 20*64-1:
            ckout = 20*64-1
        ck_time[ckin] += 1
        ck_time[ckout] -= 1
    return max(c_s(ck_time))