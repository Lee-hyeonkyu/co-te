<<<<<<< HEAD
e = 8
starts = [1, 3, 7]


# def solution(e, starts):
#     answer = []
#     return answer

cnt = 1
for i in range(1, e+1):
    x = i * cnt
    print(x)
=======
# 약수구하는 과정을 만들기
# 8의 약수 구하기.
# 방법 1. 최소의 숫자로 최대까지의 수 for문으로 그 숫자의 약수의 갯수가 많고 그 값 자체가 낮다면 저장.
e = 8

starts = [1, 3, 7]

# 시간초과

# def divisor(end):
#     tmp = []
#     start = 1
#     while start <= end:
#         for i in range(1, end+1):
#             if i * start == end:
#                 tmp.append(start)
#         start += 1
#     return len(tmp)

# def solution(e, starts):
#     answer = []

#     for s in starts:
#         div = 0
#         tmp_answer = 0
#         for i in range(s, e+1):
#             if div < divisor(i):
#                 div = divisor(i)
#                 tmp_answer = i
#         answer.append(tmp_answer)

#     return answer




def solution(e, starts):
    result = []
    divisor = [1 for _ in range(e+1)]
    memo = 0
    starts_dict = {}
    sorted_starts = sorted(starts)

    for i in range(2, e+1):
        for j in range(i, e+1, i):
            divisor[j] += 1

    for i in range(len(sorted_starts)):
        if memo == 0:
            max_index = divisor[sorted_starts[i]:].index(max(divisor[sorted_starts[i]:]))+sorted_starts[i]
            starts_dict[sorted_starts[i]] = max_index
            memo = max_index
        else:
            if sorted_starts[i] <= memo:
                starts_dict[sorted_starts[i]] = memo
            else:
                memo = divisor[sorted_starts[i]:].index(max(divisor[sorted_starts[i]:]))+sorted_starts[i]
                starts_dict[sorted_starts[i]] = memo
    
    for s in starts:
        result.append(starts_dict.get(s))
        
    return result
>>>>>>> 873c90f41b309d7b349a83daf09bf7f2fd9d118e
