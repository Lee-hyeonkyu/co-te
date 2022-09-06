# def solution(participant, completion):
#     participant.sort()
#     completion.sort()
#     for i, j in zip(participant, completion):
#         if i != j:
#             return i
#     return participant.pop()


participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]


# dict(hash사용)를 만들고 참가자의 이름을 넣은 후 중복 값이 있다면 +1
# 완주자 리스트를 돌면서 테이블 안에 있다면 -1 하면
# 0보다 key값이 크다면 완주 하지 못한 사람.

def solution(participant, completion):
    hash_list = {}
    for i in participant:
        hash_list[i] = 0
    for i in participant:
        if i in hash_list:
            hash_list[i] += 1
    for i in completion:
        if i in hash_list:
            hash_list[i] -= 1
    for i in hash_list:
        if hash_list.get(i) != 0:
            return i


print(solution(participant, completion))
