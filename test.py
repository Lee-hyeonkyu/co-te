n, k = map(int, input().split())

cnt = 0

# while 1:
#     num = (n//k) * k
#     cnt += (n - num)
#     n = num
#     if n < k:
#         break
#     cnt += 1
#     n //= k

# cnt += (n-1)

while n != 1:
    if n % k:
        cnt += 1
        n -= 1
    else:
        cnt += 1
        n //= k


print(cnt)
