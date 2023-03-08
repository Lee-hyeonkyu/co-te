def product(*lst, repeat=1):
    temp = [list(tmp) for tmp in lst] * repeat
    result = [[]]
    for tmp in temp:
        result = [x+[y] for x in result for y in tmp]
    for i in result:
        yield list(i)


def repeat(object, times=None):
    if times is None:
        while True:
            yield object
    else:
        for i in range(times):
            yield object


def solution(users, emoticons):
    answer = [0, 0]
    min_rate = 0
    switch = 1
    # 최소할인율 구하기
    while switch:
        min_rate += 10
        for i in users:
            if min_rate - i[0] > 0:
                switch = 0
    # 이모티콘 갯수만큼 경우의 수 구하기.
    n = len(emoticons)
    cases = [i for i in product(
        [i for i in range(40, min_rate-10, -10)], repeat=n)]
    # user와 cases 매칭 후 같은 위치의 emoticons의 할인율 계산한 값을 더함.
    for case in cases:
        tmp = [0, 0]
        for user in users:
            price = 0
            for i in range(n):
                if user[0] <= case[i]:
                    price += emoticons[i] - (emoticons[i]*case[i]/100)
            if user[1] <= price:
                tmp[0] += 1
            else:
                tmp[1] += price
        if tmp[0] > answer[0]:
            answer = tmp
        elif tmp[0] == answer[0] and tmp[1] > answer[1]:
            answer = tmp

    return answer
