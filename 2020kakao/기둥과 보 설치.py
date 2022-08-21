n = 5
build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]

def solution(n, build_frame):
    answer = []
    for x,y,a,b in build_frame:
        if b == 1:
            answer += [[x,y,a]]
    print(answer)


print(solution(n,build_frame))