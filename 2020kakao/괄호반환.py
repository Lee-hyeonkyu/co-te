p = "()))((()"


def check_w(s):
    cnt = 0
    for i in s:
        if i == "(":
            cnt += 1
        elif i == ")":
            cnt -= 1
            if cnt < 0:
                return False
    if cnt == 0:
        return True
    else:
        return False

# 순서가 틀렸다면 앞과 끝을 빼고 교정


def adjust_w(word):
    lst = list(word)
    lst.pop(0)
    lst.pop(-1)
    if len(lst) == 0:
        return []
    else:
        for i in range(len(lst)):
            if lst[i] == '(':
                lst[i] = ')'
            else:
                lst[i] = '('
        return lst


# 분리 함수


def split_w(word):
    cnt = 0
    for i in range(len(word)):
        if word[i] == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            cnt = i
            break

    return word[:cnt+1], word[cnt+1:]


def solution(p):
    if not p:
        return ""

    u, v = split_w(p)

    if check_w(u):
        return u + solution(v)
    else:
        return "(" + solution(v) + ")" + "".join(adjust_w(u))


print(solution(p))
