from collections import defaultdict


arrows = [6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]


def solution(arrows):
    pos = [(-1, 0), (-1, 1), (0, 1), (1, 1),
           (1, 0), (1, -1), (0, -1), (-1, -1)]
    answer = 0
    return answer


# 방법1. arrows의 다음 숫자가 변하면 그 변화점이 꼭지점이된다. 같은 숫자 반복의 3이상의 패턴과
# 그 반복수가 이전의 크기를 넘었다면 하나의 도형 생성됨.
# 문제 . 밖으로 꼬아 들어온 도형은 모르겠다.
