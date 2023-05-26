picks = [1, 3, 2]
minerals = ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]


def solution(picks, minerals):
    p_cnt = []
    answer = 0
    # 곡괭이가 캘 수 있는 광물보다 갯수가 많으면 알맞게 자르기
    if sum(picks) * 5 < len(minerals):
        minerals = minerals[: sum(picks) * 5]
    cut = 0
    # 한 곡괭이당 5개를 캘 수 있으니까 리스트 5개씩 잘라주기
    while cut < len(minerals):
        tmp = minerals[cut : cut + 5]
        l_tmp = len(tmp)
        cnt = 0
        # 비교가 가능한 돌괭이 기준으로 값을 저장
        for i in tmp:
            if i[0] == "d":
                cnt += 25
            elif i[0] == "i":
                cnt += 5
            else:
                cnt += 1
        # 최대괭이질과 광물 갯수 저장
        p_cnt.append([cnt, l_tmp])
        # 5씩 자르려고 5씩 더해줌
        cut += 5
    # 정렬해서 뒤부터 pop해서 사용하려고 저장
    p_cnt.sort()
    # 다이아, 아이언, 스톤 순 괭이 확인하려고 사용
    for i, j in enumerate(picks):
        # 괭이가 존재하면
        if j:
            # 그 갯수만큼 반복
            for _ in range(j):
                # 캘 광물도 존재하는지 확인 (광물보다 괭이가 더 많을 수 있으니까요)
                if p_cnt:
                    kang = p_cnt.pop()
                    # 다이아라면 그냥 갯수만큼 더해주기
                    if i == 0:
                        answer += kang[1]
                    # 돌이라면
                    elif i == 1:
                        # 그 길이가 5보다 작으면 한방에 캘 수 있으니 광물 수 더하기
                        if kang[0] <= 5:
                            answer += kang[1]
                        # 아니면 5로 떨어지면 다이아 아니면 돌이니까 나머지 플러스
                        else:
                            answer += kang[0] // 5
                            answer += kang[0] % 5
                    # 돌이면 그냥 최대횟수 플러스
                    else:
                        answer += kang[0]

    return answer
