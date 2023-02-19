n = int(input())
lst = list(map(int, input().split()))
if n % 2:
    n = (n//2)+1
else:
    n //= 2

print(sorted(lst)[n-1])
