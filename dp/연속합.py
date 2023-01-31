n = int(input())

array = list(map(int, input().split()))

for i in range(1, n):
    array[i] = max(array[i], array[i]+array[i-1])

print(max(array))
print(array)

d = [0] * 100_000

result = array[0]
for j in range(n):
    d[j] = array[j] + d[j-1]
    result = max(result, d[j])

for i in range(n-1):
    for j in range(i+1, n):
        d[j] -= d[i]
        result = max(result, d[j])
print(result)
