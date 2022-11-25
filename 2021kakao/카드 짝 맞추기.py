board = [[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]]
r = 1
c = 0

# start지점이 0이 아니라면 cnt += 1
# start지점이 0이라면  가로 탐색? 후 세로탐색? 

def solution(board, r, c):
    start_point = board[r][c]
    cnt = 0
    if start_point != 0:
        cnt += 1 
    else:


    answer = 0
    return answer


print(solution(board, r, c))
