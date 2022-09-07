numbers = [1, 1, 1, 1, 1]
target = 3


def solution(numbers, target):
    answer = 0
    bfs = [0]

    for i in numbers:
        tmp = []
        for j in bfs:
            tmp.append(j+i)
            tmp.append(j-i)
        bfs = tmp

    for node in bfs:
        if node == target:
            answer += 1
    return answer


print(solution(numbers, target))


def solution(numbers, target):
    answer = DFS(numbers, target, 0)
    return answer


def DFS(numbers, target, depth):
    answer = 0
    if depth == len(numbers):
        print(numbers)
        if sum(numbers) == target:
            return 1
        else:
            return 0
    else:
        answer += DFS(numbers, target, depth+1)
        numbers[depth] *= -1
        answer += DFS(numbers, target, depth+1)
        return answer
