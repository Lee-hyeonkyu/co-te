def solution(answers):
    st_1 = [1, 2, 3, 4, 5] * 2000
    st_2 = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    st_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000

    cnt_1, cnt_2, cnt_3 = 0, 0, 0

    for i in range(len(answers)):
        if st_1[i] == answers[i]:
            cnt_1 += 1
        if st_2[i] == answers[i]:
            cnt_2 += 1
        if st_3[i] == answers[i]:
            cnt_3 += 1

    lst = [cnt_1, cnt_2, cnt_3]

    print(max(lst))


answers = [1, 2, 3, 4, 5]

solution(answers)
