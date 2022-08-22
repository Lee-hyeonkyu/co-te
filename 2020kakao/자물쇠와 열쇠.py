import copy

key = [[0, 0, 0], [1, 0, 0],[0,1,1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

def check(space,k,n):
    for i in range(n):
        for j in range(n):
            if space[k+i][k+j] != 1:
                return False
    return True

def test(space, k_rota, k,n):
    s = len(k_rota[0])
    for i in range(4):
        for h in range(k+n):
            for v in range(k+n):
                space1 = copy.deepcopy(space)
                for x in range(s):
                    for y in range(s):
                        space1[h+x][v+y] += k_rota[i][x][y]
                if check(space1,k,n):
                    return True
    return False

def solution(key, lock):
    # key 회전
    k_rota = [
        key,
        list(zip(*reversed(key))),
        list(map(lambda x:list(reversed(x)), reversed(key))),
        list(reversed(list(map(list,zip(*key)))))
    ]

    k = len(key)-1
    n = len(lock)
    # key와 lock 만큼의 크기 할당
    space = [[0 for _ in range(k*2 + n)]for _ in range(k*2+n)]
    for i in range(n):
        for j in range(n):
            space[k+i][k+j] = lock[i][j]
    
    if test(space, k_rota, k,n) == True:
        return True
    else:
        return False

print(solution(key,lock))



'''
import copy

def check(space1,k,n):
    for i in range(n):
        for j in range(n):
            if space1[k+i][k+j] != 1:
                return False
    return True

def test(space1, k_rota, i, j, x,k,n):
    s = len(k_rota[0])
    for h in range(s):
        for v in range(s):
            space1[i+h][j+v] += k_rota[x][h][v]
    if check(space1,k,n) == True:
        return True
    return False
    




def solution(key, lock):
    # key 회전
    k_rota = [
        key,
        list(zip(*reversed(key))),
        list(map(lambda x:list(reversed(x)), reversed(key))),
        list(reversed(list(map(list,zip(*key)))))
    ]

    k = len(key)-1
    n = len(lock)
    # key와 lock 만큼의 크기 할당
    space = [[0 for _ in range(k*2 + n)]for _ in range(k*2+n)]
    for i in range(n):
        for j in range(n):
            space[k+i][k+j] = lock[i][j]

    for i in range(k+n):
        for j in range(k+n):
            for x in range(4):
                space1 = copy.deepcopy(space)

                if test(space1, k_rota, i, j, x,k,n) == True:
                    return True


                

    return False
'''