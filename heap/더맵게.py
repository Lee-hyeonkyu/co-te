import heapq

scoville= [1, 2, 3, 9, 10, 12]
K = 7

def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        if len(scoville)> 1:
            cnt +=1
            heapq.heappush(scoville,heapq.heappop(scoville)+(heapq.heappop(scoville)*2))
        else:
            return -1
    # print(scoville)
    return cnt


# 효율성 테스트 통과 X (시간 초과)
# def solution(scoville, K):
#     cnt = 0
#     while min(scoville) < K:
#         if len(scoville) == 1: 
#             return -1 
#         cnt +=1
#         heapq.heapify(scoville)
#         heapq.heappush(scoville,heapq.heappop(scoville)+(heapq.heappop(scoville)*2))
    
#     # print(scoville)
#     return cnt


# 효율성 테스트는 통과 정확성 1,3,8,13  X
# def solution(scoville, K):
#     cnt = 0
#     heapq.heapify(scoville)
#     if len(scoville) == 1: 
#         return -1 
#     while scoville[0] < K:
#         cnt +=1
#         heapq.heappush(scoville,heapq.heappop(scoville)+(heapq.heappop(scoville)*2))
    
#     return cnt



print(solution(scoville, K))