priorities = [2, 1, 3, 2]
location = 2


def solution(priorities, location):
    li = []  # 순번 담고 있는 리스트

    for i in range(len(priorities)):
        li.append([priorities[i], i])

    lis = []  # 중요도 순 리스트

    while len(li) != 0:
        if li[0][0] == max(li)[0]:
            lis.append(li[0])
            li.remove(li[0])
        else:
            li.append(li[0])
            li.remove(li[0])
    return lis.index([priorities[location], location]) + 1
