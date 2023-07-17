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