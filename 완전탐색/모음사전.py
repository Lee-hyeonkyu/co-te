from itertools import product


def solution(word):
    x = ["A", "E", "I", "O", "U"]

    dic = []
    for i in range(1, 6):
        for j in list(product(x, repeat=i)):
            dic.append("".join(j))
    dic.sort()

    answer = dic.index(word)+1
    return answer
