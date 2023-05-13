from collections import deque

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]


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

##########################2023-05-13########


from collections import deque

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]


def solution(begin, target, words):
    # 타겟이 그룹에 존재하지 않을 때
    if target not in words:
        return 0
    l = len(words)
    w_l = len(words[0])
    visited = [False for _ in range(l)]
    q = deque()
    q.append([begin, 0])

    while q:
        n_word, cnt = q.popleft()
        if n_word == target:
            return cnt
        # 그룹의 길이만큼 반복
        for i in range(l):
            # 아직 방문하지 않은 곳 확인
            if not visited[i]:
                # 일치하는 스펠 수
                tmp_cnt = 0
                # 단어의 길이만큼 반복
                for lenght in range(w_l):
                    # 가지고 있는 단어와 그룹의 단어가 일치하는 개수 체크
                    if n_word[lenght] == words[i][lenght]:
                        tmp_cnt += 1
                if tmp_cnt == w_l - 1:
                    q.append([words[i], cnt + 1])
                    visited[i] = True


print(solution(begin, target, words))
