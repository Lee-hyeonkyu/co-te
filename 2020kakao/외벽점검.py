from itertools import permutations
from collections import deque
n = 12
weak = [1,5,6,10]
dist = [1,2,3,4]


# def solution(n, weak, dist):
#     q = deque()
#     idiots = len(dist)
#     answer = -1

#     for idx,w in enumerate(weak):
#         q.append((weak[:idx] + weak[idx + 1:], dist[:-1], w, dist[-1]))
#     while len(q)> 0:
#         left_w, left_i, now_w, now_i = q.popleft()
#         c,rc = left_w[:],left_w[:]
#         c_n, rc_n = 0,0
#         for i in range(now_w, now_i + now_w+1):
#             if i >= n:
#                 i -= n
#             if i in c:
#                 c_n +=1
#                 c.remove(i)
#         for i in range(now_w, now_w - now_i-1):
#             if i < 0:
#                 i += n
#             if i in rc:
#                 rc_n += 1
#                 rc.remove(i)
#         if len(c) == 0 or len(rc) == 0:
#             answer = idiots - len(left_i)
#             break
#         if len(left_i) > 0:
#             if not (c_n < 1 and len(c) > len(left_i)):
#                 for idx,w in enumerate(c):
#                     q.append((c[:idx] + c[idx+1:], left_i[:-1],w,left_i[-1]))
#             if not (rc_n < 1 and len(rc) > len(left_i)):
#                 for idx, w in enumerate(rc):
#                     q.append((rc[:idx]+ rc[idx+1:], left_i[:-1],w,left_i[-1]))
#     return answer


# print(solution(n, weak, dist))

def solution(n,weak,dist):
    people = 9
    w_s = len(weak)
    weak = weak + [w+n for w in weak]
    print(weak)
    for i in range(w_s):
        for p in permutations(dist, len(dist)):
            print(p)
            cnt = 1
            current = i
            for j in range(1, w_s):
                next = i + j
                distance = weak[next] - weak[current]
                if distance > p[cnt-1]:
                    current = next
                    cnt +=1
                    if cnt > len(dist):
                        break
            if cnt <= len(dist):
                people = min(people, cnt)
    if people == 9:
        return -1

    return people


print(solution(n,weak,dist))