from itertools import product


def solution(user_id, banned_id):
    ban_check = [[] for _ in range(len(banned_id))]
    for i in range(len(banned_id)):
        for user in user_id:
            if len(banned_id[i]) == len(user):
                switch = 1
                for p in range(len(banned_id[i])):
                    check = list(set(banned_id[i][p]) - set(user[p]))
                    if len(check) and check != ["*"]:
                        switch = 0
                        break
                if switch:
                    ban_check[i].append(user)
    ban_id = list(product(*ban_check))
    answer = len({tuple(sorted(u)) for u in ban_id if len(set(u)) == len(u)})

    return answer
