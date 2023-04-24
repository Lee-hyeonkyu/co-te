commands = ["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2",
            "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]


def update(com, board):
    # 위치 값으로 업데이트
    if len(com) == 4:
        if board[int(com[1])-1][int(com[2])-1]:
            tmp = board[int(com[1])-1][int(com[2])-1]
            for i in range(50):
                for j in range(50):
                    if board[i][j] == tmp:
                        board[i][j] = com[3]
        else:
            board[int(com[1])-1][int(com[2])-1] = com[3]
    else:
        for i in range(50):
            for j in range(50):
                if board[i][j] == com[1]:
                    board[i][j] = com[2]
    return board


def merge(com, board, merge_cnt):
    # 같은 위치라면 merge할 필요 x
    # if com[1] == com[3] and com[2] == com[4]:
    #     return board
    if board[int(com[1])-1][int(com[2])-1] == board[int(com[3])-1][int(com[4])-1]:
        return board
    # 첫번째 인덱스 위치에 값이 있다면 그 값을 두번째 인덱스의 위치에도 넣어주기
    if board[int(com[1])-1][int(com[2])-1]:
        # 또 두번째 인덱스가 이미 merge된 셀이라면 나머지 셀도 다같이 합쳐줘야함.
        if board[int(com[3])-1][int(com[4])-1]:
            tmp = board[int(com[3])-1][int(com[4])-1]
            for i in range(50):
                for j in range(50):
                    if board[i][j] == tmp:
                        board[i][j] = board[int(com[1])-1][int(com[2])-1]
        else:
            board[int(com[3])-1][int(com[4]) -
                                 1] = board[int(com[1])-1][int(com[2])-1]
    # 그게 아니라면
    elif board[int(com[3])-1][int(com[4])-1]:
        board[int(com[1])-1][int(com[2]) -
                             1] = board[int(com[3])-1][int(com[4])-1]
    else:
        board[int(com[1])-1][int(com[2])-1] = merge_cnt
        board[int(com[3])-1][int(com[4])-1] = merge_cnt
        merge_cnt += 1

    return board, merge_cnt


def unmerge(com, board):
    tmp = board[int(com[1])-1][int(com[2])-1]
    for i in range(50):
        for j in range(50):
            if board[i][j] == tmp:
                board[i][j] = 0
    board[int(com[1])-1][int(com[2])-1] = tmp

    return board


def solution(commands):
    merge_cnt = 9999999999
    answer = []
    board = [[0]*50 for _ in range(50)]
    for i in commands:
        com = i.split(" ")
        if com[0] == "UPDATE":
            update(com, board)
        elif com[0] == "MERGE":
            merge(com, board, merge_cnt)
        elif com[0] == "UNMERGE":
            unmerge(com, board)
        else:
            # if not board[int(com[1])-1][int(com[2])-1]:
            #     answer.append("EMPTY")
            if type(board[int(com[1])-1][int(com[2])-1]) == int:
                answer.append("EMPTY")
            else:
                answer.append(str(board[int(com[1])-1][int(com[2])-1]))
    return answer


# board를 만들고 50 x 50 구조에 딕셔너리형태로 1번부터 250번까지 번호를 만들고 그 고유값에
# 값을 추가 및 제거 하면 가능?
print(solution(commands))
