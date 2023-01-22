# def solution(answers):
#     st_1 = [1, 2, 3, 4, 5] * 2000
#     st_2 = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
#     st_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000

#     cnt_1, cnt_2, cnt_3 = 0, 0, 0

#     for i in range(len(answers)):
#         if st_1[i] == answers[i]:
#             cnt_1 += 1
#         if st_2[i] == answers[i]:
#             cnt_2 += 1
#         if st_3[i] == answers[i]:
#             cnt_3 += 1

#     lst = [cnt_1, cnt_2, cnt_3]

#     print(max(lst))


# answers = [1, 2, 3, 4, 5]

# solution(answers)


answers = [1, 2, 3, 4, 5]


def solution(answers):
    one = [1, 2, 3, 4, 5] * 2000
    two = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    student = [one, two, three]
    correct = 0
    answer = []
    for i in range(len(student)):
        cnt = 0
        for j in range(len(answers)):
            if answers[j] == student[i][j]:
                cnt += 1
        if cnt > correct:
            correct = cnt
            answer = []
            answer.append(i+1)
        elif cnt == correct:
            answer.append(i+1)

    return answer
