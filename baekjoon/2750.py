n = int(input())
arr = []

for i in range(n):
    x = int(input())
    arr.append(x)
    arr = sorted(arr)

for i in range(n):
    print(arr[i])