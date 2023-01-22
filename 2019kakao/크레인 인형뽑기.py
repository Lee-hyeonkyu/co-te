def solution(board, moves):
    answer = 0
    lst = []
    epochs = len(moves)
    for i in moves:
        for j in board:
            if j[i-1]:
                lst.append(j[i-1])
                j[i-1] = 0
                break
    while epochs:
        for i in range(len(lst)-1):
            if lst[i] == lst[i+1]:
                answer += 2
                del lst[i:i+2]
                epochs -= 1
                break
        epochs -= 1
    return answer
