from collections import defaultdict


k = 2
id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo", "apeach frodo", "frodo neo",
          "muzi neo", "apeach muzi", "muzi frodo"]


def solution(id_list, report, k):
    report = list(set(report))
    dic = defaultdict()
    answer = []
    for i in report:
        x = i.split()
        if x[1] in dic:
            dic[x[1]] += [x[0]]
        else:
            dic[x[1]] = [x[0]]

    for i in id_list:
        cnt = 0
        for j in dic:
            if len(dic[j]) >= k:
                if i in dic[j]:
                    cnt += 1
        answer.append(cnt)

    return answer


print(solution(id_list, report, k))
