board = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,4,0,0,0],[0,0,0,0,0,4,4,0,0,0],[0,0,0,0,3,0,4,0,0,0],[0,0,0,2,3,0,0,0,5,5],[1,2,2,2,3,3,0,0,0,5],[1,1,1,0,0,0,0,0,0,5]]






# 탐색 함수 row col height
def exist(r,c,h):
    # 블록의 숫자(0~200)
    block_num = -1
    cnt = 0
    # 2,3 모양의 블록
    if h == 2:
        for i in range(r,r + h):
            for j in range(c,c+h+1):
                if board1[i][j] == 0:
                    # 위가 비어있다면 cnt +1
                    for x in range(i):
                        if board1[x][j] != 0:
                            return False
                    cnt += 1
                    # 6-4 = 2 이상은 다른 블록과 함께
                    if cnt > 2:
                        return False
                else:
                    if block_num == -1:
                        block_num = board1[i][j]
                    elif block_num != board1[i][j]:
                        return False

        for i in range(r,r + h):
            for j in range(c,c+h+1):
                board1[i][j] = 0
        return True
    # 3,2 모양의 블록
    else:
        for i in range(r,r+h):
            for j in range(c,c+h-1):
                if board1[i][j] == 0:
                     # 위가 비어있다면 cnt +1
                    for x in range(i):
                        if board1[x][j] != 0:
                            return False
                    cnt += 1
                    # 6-4 = 2 이상은 다른 블록과 함께
                    if cnt > 2:
                        return False
                else:
                    if block_num == -1:
                        block_num = board1[i][j]
                    elif block_num != board1[i][j]:
                        return False
        for i in range(r,r + h):
            for j in range(c,c+h+1):
                board1[i][j] = 0
        return True




def solution(board):
    global board1
    board1 = board
    answer= 0
    # n*n의 크기를 가진 범위
    n = len(board)
    # 범위를 탐색하는 루프, 도형을 지우고 다시 사용. 
    while 1:
        cnt = 0
        # 범위 탐색 0,0 -> 10,10까지
        for i in range(n):
            for j in range(n):
                # 찾던 도형의 모양이 존재한다면 +1
                if i<= n-2 and j<= n-3 and exist(i,j,2):
                    cnt +=1
                elif i<= n-3 and j<= n-2 and exist(i,j,3):
                    cnt +=1
        answer += cnt
        # 찾는 블록이 없었다면 지워진 블록이 없으니 중지
        if cnt == 0:
            break
    
    return answer


# print(solution(board))
'''---------------------'''




# # 탐색 함수 row col height
# def exist(r,c,h,w):
#     # 블록의 숫자(0~200)
#     block_num = -1
#     cnt = 0
#     for i in range(r,r + h):
#         for j in range(c,c+w):
#             if board1[i][j] == 0:
#                 # 위가 비어있다면 cnt +1
#                 for x in range(i):
#                     if board1[x][j] != 0:
#                         return False
#                 cnt += 1
#                 # 6-4 = 2 이상은 다른 블록과 함께
#                 if cnt > 2:
#                     return False
#             else:
#                 if block_num == -1:
#                     block_num = board1[i][j]
#                 elif block_num != board1[i][j]:
#                     return False

#     for i in range(r,r + h):
#         for j in range(c,c+h+1):
#             board1[i][j] = 0
#     return True



# def solution(board):
#     global board1
#     board1 = board
#     answer= 0
#     # n*n의 크기를 가진 범위
#     n = len(board)
#     # 범위를 탐색하는 루프, 도형을 지우고 다시 사용. 
#     while 1:
#         cnt = 0
#         # 범위 탐색 0,0 -> 10,10까지
#         for i in range(n):
#             for j in range(n):
#                 # 찾던 도형의 모양이 존재한다면 +1
#                 if i<= n-2 and j<= n-3 and exist(i,j,2,3):
#                     cnt +=1
#                 elif i<= n-3 and j<= n-2 and exist(i,j,3,2):
#                     cnt +=1
#         answer += cnt
#         # 찾는 블록이 없었다면 지워진 블록이 없으니 중지
#         if cnt == 0:
#             break
    
#     return answer

print(solution(board))
