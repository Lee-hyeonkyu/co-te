from collections import defaultdict


def solution(friends, gifts):
    points = [0] * len(friends)
    answer = [0] * len(friends)
    gifts = [i.split() for i in gifts]
    gift_card = [[0] * len(friends) for _ in range(len(friends))]

    name_number = {j: i for i, j in enumerate(friends)}
    for i, j in gifts:
        gift_card[name_number[i]][name_number[j]] += 1
        points[name_number[i]] += 1
        points[name_number[j]] -= 1

    for i in range(len(friends)):
        for j in range(i + 1, len(friends)):
            if gift_card[i][j] > gift_card[j][i]:
                answer[i] += 1
            elif gift_card[i][j] < gift_card[j][i]:
                answer[j] += 1
            else:
                if points[i] > points[j]:
                    answer[i] += 1
                elif points[i] < points[j]:
                    answer[j] += 1
    return max(answer)
