number='654321'
k= 5
def solution(number, k):
    x = []
    cnt = 0

    for i in number:
        if cnt != k:
            if len(x) == 0:
                x.append(i)
            else:
                while len(x) != 0:
                    if cnt == k or i <= x[-1]:
                        break
                    elif i> x[-1]:
                        x.pop()
                        cnt+=1
                x.append(i)
        else:
            x.append(i)

    while cnt !=k:
        x.pop()
        cnt+=1

    return "".join(x)





print(solution(number, k))