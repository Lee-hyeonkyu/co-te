

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
