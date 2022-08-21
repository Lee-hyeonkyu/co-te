def solution(record):
    chatrm = {} # 채팅방에 들어온 유저
    records = [] #리스트 분리
    alert = [] # 알림창
    
    # 분리하기
    for i in record:
        records.append(i.split(" "))

    # chatrm에 유저 넣기
    for i in records:
        if i[0] == 'Enter' or i[0]== 'Change':
            chatrm[i[1]] = i[2]

    # chatrm으로 저장된 유저닉네임으로 알림창으로 저장 
    for i in records:
        if i[0] == "Enter":
            alert.append(f"{chatrm[i[1]]}님이 들어왔습니다.")
        elif i[0] == 'Leave':
            alert.append(f"{chatrm[i[1]]}님이 나갔습니다.")
    return alert