def solution(s):

    res = []
    # 최대 반복 길이
    n = len(s)//2

    if len(s) == 1:
        return 1
    # 최대길이 반복문
    for i in range(1, n+1):
        string = ''
        cnt = 1
        tmp = s[:i]

        # i 부터 i 이후의 문자열 끝까지 도는 반복문
        for j in range(i, len(s), i):
            # 반복되는 문자열과 같은지 확인 
            if tmp== s[j:i+j]:
                cnt +=1
            else:
                # 길이가 1이면 숫자없이 문자만 아니면 숫자와 문자 
                if cnt == 1:
                    string += tmp
                else:
                    string += str(cnt) + tmp
                # tmp 업데이트
                tmp = s[j:i+j]
                # 반복 카운트 초기화
                cnt = 1
        # print(string)
        if cnt == 1:
            string += tmp
        else:
            string += str(cnt) + tmp
        # print(string)
        res.append(len(string))
    return min(res)