from bisect import bisect_left


info = ["java backend junior pizza 150",
        "python frontend senior chicken 210",
        "python frontend senior chicken 150",
        "cpp backend senior pizza 260",
        "java backend junior chicken 80",
        "python backend senior chicken 50"
        ]
query = ["java and backend and junior and pizza 100",
         "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250",
         "- and backend and senior and - 150",
         "- and - and - and chicken 100",
         "- and - and - and - 150"
         ]

# 효율성 0 점

# def solution(info, query):
#     answer = []
#     pre_query = []
#     pre_info = []
#     for i in query:
#         pre_query.append(i.split(" "))
#     for i in info:
#         pre_info.append(i.split(" "))

#     for i in pre_query:
#         tmp = 0
#         food = i[6]
#         career = i[4]
#         position = i[2]
#         lang = i[0]
#         score = int(i[7])
#         if score == "-":
#             score = int(0)
#         for j in pre_info:
#             r_score =int(j[-1])
#             if score <= r_score:
#                 if food in j or food == "-":
#                     if career in j or career == "-":
#                         if position in j or position == "-":
#                             if lang in j or lang == "-":
#                                 tmp += 1
#         answer.append(tmp)


#     return answer

# print(solution(info,query))

def solution(info, query):
    hable = dict()
    for lang in ['java', 'python', 'cpp', '-']:
        for pos in ['frontend', 'backend', '-']:
            for car in ['junior', 'senior', '-']:
                for food in ['pizza', 'chicken', '-']:
                    hable.setdefault((lang, pos, car, food), [])

    print(hable)
    for i in info:
        [lang, pos, car, food, score] = i.split()
        for lan in [lang, '-']:
            for p in [pos, '-']:
                for c in [car, '-']:
                    for f in [food, '-']:
                        hable[(lan, p, c, f)].append(int(score))

    print(hable)
    for sco in hable.values():
        sco.sort()
    print()
    print(hable)
    result = []
    for q in query:
        conts = q.split()
        scos = int(conts[-1])
        [ll, pp, cc, ff] = [conts[0], conts[2], conts[4], conts[6]]
        result.append(len(hable[(ll, pp, cc, ff)])
                      - bisect_left(hable[(ll, pp, cc, ff)], scos))

    return result


print(solution(info, query))
