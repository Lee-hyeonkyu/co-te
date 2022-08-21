array = [1, 5, 2, 6, 3, 7, 4]
commands =[[2, 5, 3], [4, 4, 1], [1, 7, 3]]

def solution(array, commands):
    answer = []
    for i in commands:
        a = sorted(array[i[0]-1:i[1]])
        if len(a) == 1:
            answer.append(a[0])
        else:
            answer.append(a[i[2]-1])

    return answer

print(solution(array,commands))

# for i in commands:
#     a = sorted(array[i[0]-1:i[1]])
#     if len(a) == 1:
#         print(a[0])
#     else:
#         print(a[i[2]-1])
