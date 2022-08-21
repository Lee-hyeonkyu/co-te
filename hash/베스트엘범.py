genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]


def solution(genres, plays):
    answer = []
    play_t = {}
    order_g = {}

    for i, (x, y) in enumerate(zip(genres, plays)):
        if x in play_t:
            play_t[x] += y
        else:
            play_t[x] = y
       
        if x in order_g:
            order_g[x].append((y, i))
        else:
            order_g[x] = [(y, i)]
        
    play_t = sorted(play_t.items(), key = lambda x: x[1], reverse = True)
    
    print(play_t)
    print(order_g)

    for i in play_t:
        order_g[i[0]] = sorted(order_g[i[0]], key = lambda x: x[0], reverse = True)[:2]
        for (x,y) in order_g[i[0]]:
            answer.append(y)
    print(answer)
solution(genres, plays)


'''
처음 시도했던 방법 answer에 추가하는 부분에서 입출력 예시 였던 genres의 리스트 길이가 길어지면 list index out of range 가 나서 문제였던것.
def solution(genres, plays):
    answer = []
    play_time = {} # 총 플레이 수
    order_g = {} # 장르별 순서와 플레이 수

    for i in range(len(genres)):
        if genres[i] in play_time.keys():
            play_time[genres[i]]+=plays[i]
            order_g[genres[i]].append((plays[i],i))   
        else:
            play_time[genres[i]] = plays[i]
            order_g[genres[i]] = [(plays[i],i)]
           
    play_time = sorted(play_time.items(), key = lambda x: x[1], reverse = True)
    
    #  문제였던 부분
    # for i in play_time:
    #     order_g[i[0]] = sorted(order_g[i[0]], key = lambda x: x[0], reverse = True)
    #     for j in range(len(order_g)):
    #         if j == 2:
    #             break
    #         answer.append(order_g[i[0]][j][1])

    #고친부분 
    for i in play_time:
        order_g[i[0]] = sorted(order_g[i[0]], key = lambda x: x[0], reverse = True)[:2]
        for (x,y) in order_g[i[0]]:
            answer.append(y)
  
    return(answer)
    
    
genres = ["classic", "pop", "classic", "classic", "pop", "k-pop"]
plays = [500, 600, 150, 800, 2500, 4000]

print(solution(genres, plays))

'''