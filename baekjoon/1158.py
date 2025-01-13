n, k = map(int, input().split())

arr = [i for i in range(1, n + 1)]

answer = []

iteration = 0
while arr:
    iteration = (iteration + k - 1) % len(arr)
    answer.append(arr.pop(iteration))

print("<" + str(answer)[1:-1] + ">")
