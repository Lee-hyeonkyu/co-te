from itertools import permutations


def prime(num):
    if num== 0 or num == 1:
        return False
    elif num == 2:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
    return True 

def solution(numbers):
    answer = 0
    all = []

    for i in range(len(numbers)):
        temp = list(permutations(numbers,i+1))
        all += [int(''.join(i)) for  i in temp]
    print(all)
    all = set(all)
    print(all)
    for i in all:
        if prime(i):
            answer+= 1
    print(answer)

numbers= "011"
solution(numbers)