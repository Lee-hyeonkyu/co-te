from collections import deque

# 3, 4, 2, 3, 3, 1, 5
n = 6
m = 6
x = 2
y = 6
r = 6
c = 5
k = 11
'''
우선순위
1. d 하
2. l 좌
3. r 우
4. u 상
최단거리로 먼저 끝점에 도착. 일반적인 bfs but, 
'''


'''
1. answer는 저장한 배열을 sort해서 0번째 인덱스 꺼내오면 그게 답.
2. 문자열을 어디에 저장을 할 것인가.
3. 생각나는 방법 1. 최소 거리를 저장하고 만약  k = 10인데  5안에 도착했다면 나머지 최소값으로 반복 어떤데. 안됨. 
이유: luurr와 uurlr 를 비교하면 1번이 더 빠르기 때문 목적지 도착은 2번이 더 빨리 도착하고 나머지를 반복함.



'''


def solution(n, m, x, y, r, c, k):
    q = deque()
    dx = [1, 0, 0, -1]
    dy = [0, -1, 1, 0]
    fang = ["d", "l", "r", "u"]
    if (abs(x-r)+abs(y-c) - k) % 2 or abs(x-r)+abs(y-c) > k:
        return "impossible"
    q.append([x-1, y-1, ""])
    while q:
        x_, y_, text = q.popleft()
        if [x_, y_] == [r-1, c-1] and len(text) == k:
            return text
        for i in range(4):
            nx = x_ + dx[i]
            ny = y_ + dy[i]
            if 0 <= nx < n and 0 <= ny < m and abs(nx - (r-1)) + abs(ny - (c-1)) + len(text)+1 <= k:
                q.append([nx, ny, text+fang[i]])
                break
    return "impossible"
