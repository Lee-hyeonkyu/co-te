words = ["go", "gone", "guild"]


def solution(words):
    dic = {}
    for word in words:
        ct = dic

        for spell in word:
            ct.setdefault(spell, [0, {}])

            ct[spell][0] += 1
            ct = ct[spell][1]

    result = 0

    for word in words:
        ct = dic
        for i in range(len(word)):
            if ct[word[i]][0] == 1:
                break
            ct = ct[word[i]][1]
            print(ct)

        result += i + 1
    return result


print(solution(words))
