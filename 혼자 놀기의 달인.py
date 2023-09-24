

cards = [8,6,3,7,2,5,1,4]



def solution(cards):
    x = [0]*len(cards)
    cnt = 0
    tmp = 0
    i = 0
    lst = []
    while 1:
        if not x[i]:
            x[i] = 1
            tmp += 1
            i = cards[i]-1
        else:
            cnt += 1
            i = cnt
            lst.append(tmp)
            tmp = 0
        if not x.count(0):
            if tmp:
                lst.append(tmp)
            break
    
    if len(lst) <= 1:
        return 0
    lst.sort(reverse=True)
    if lst[1]:
        answer = lst[0] * lst[1]
    else:
        answer = lst[0]
    return answer

############################다른 사람의 풀이#####



def solution(cards):
    answer = []
    for i in range(len(cards)):
        tmp = []
        while cards[i] not in tmp:
            tmp.append(cards[i])
            i = cards[i] - 1
        answer.append([] if sorted(tmp) in answer else sorted(tmp))
    answer.sort(key=len)
    
    return len(answer[-1]) * len(answer[-2])
    

print(solution(cards))