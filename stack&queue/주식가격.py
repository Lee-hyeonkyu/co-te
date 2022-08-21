from tkinter import SOLID


prices= [1, 2, 3, 2, 3]

def solution(prices):
    answer = [0]* len(prices)
    a = []

    for i , x in enumerate(prices):
        while a and x < prices[a[-1]]:
            j = a.pop()
            answer[j] = i- j
        a.append(i)

    while a:
        i = a.pop()
        answer[i] = len(prices) -1 -i
    
    return answer

print(solution(prices))