from collections import deque

begin = 'hit'
target = 'cog'
words = ["hot", "dot", "dog", "lot", "log", 'cog']


def solution(begin, target, words):
    if target not in words:
        return 0
    answer = 0
    q = deque()
    q.append([begin, 0])
    x = [0 for i in range(len(words))]

    while q:
        word, cnt = q.popleft()
        if word == target:
            answer = cnt
            break
        for i in range(len(words)):
            t_cnt = 0
            if not x[i]:
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        t_cnt += 1
                if t_cnt == 1:
                    q.append([words[i], cnt + 1])
                    x[i] = 1

    return answer


print(solution(begin, target, words))
