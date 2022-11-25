from collections import deque


def check_p(l_p, r_p, num):
    x_1, y_1 = l_p[0]
    x_2, y_2 = r_p[0]
    x_p, y_p = num[0]

    left = abs(x_1 - x_p) + abs(y_1 - y_p)
    right = abs(x_2 - x_p) + abs(y_2 - y_p)

    if left - right > 0:
        return "R"
    elif left - right < 0:
        return "L"
    else:
        if hand == 'right':
            return 'R'
        else:
            return 'L'


def solution(numbers, hand):
    l_p, r_p = deque(), deque()
    pad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [-1, 0, -2]]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    l = [1, 4, 7]
    r = [3, 6, 9]
    l_p.append([3, 0])
    r_p.append([3, 2])
    answer = ''
    lft = 0
    rht = 0
    for i in numbers:
        if i in l:
            answer += 'L'
            lft = i
        elif i in r:
            answer += 'R'
            rht = i
        else:
            l_p = [(i, j) for i in range(4)
                   for j in range(3) if pad[i][j] == lft]
            r_p = [(i, j) for i in range(4)
                   for j in range(3) if pad[i][j] == rht]
            next_p = [(i1, j1) for i1 in range(4)
                      for j1 in range(3) if pad[i1][j1] == i]

            pri = check_p(l_p, r_p, next_p)
            answer += pri
            if pri == 'L':
                lft = i
            else:
                rht = i
    return answer


numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = 'right'
print(solution(numbers, hand))
