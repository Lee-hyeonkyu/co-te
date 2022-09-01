h = 12
k = 3
boxes = [2, 3, 6, 7, 8, 10, 11]


def solution(h, k, boxes):
    answer = 0
    location = 0
    boxes.append(h)
    sorted(boxes)
    step = list()
    while location != h:
        able = [x for x in boxes if location + k >= x]

        if able:
            location = max(able)
            step.append(location)
        else:
            return -1

        answer = len(step) - 1

    return answer


print(solution(h, k, boxes))
