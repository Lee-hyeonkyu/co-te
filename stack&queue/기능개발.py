def solution(progresses, speeds):
    ret = [] # 배포 소요 날짜
    for i in range(len(progresses)):
        x = (100-progresses[i])//speeds[i]
        y = (100-progresses[i])%speeds[i]
        if y == 0:
            ret.append(x)
        else:
            ret.append(x+1)

    cnt = 1 # 배포 당시 가능한 작업 수
    retu = [] # return 값
    a = 0 # 첫 배포 날짜
    for i in range(1,len(ret)):
        if ret[a] >= ret[i]:
            cnt += 1
        else:
            retu.append(cnt)
            cnt = 1
            a = i
            if i == (len(ret)-1):
                retu.append(cnt)
    if cnt != 1:
        retu.append(cnt)
    return retu