num = ''
n = 125
while n:
    num += str(n % 3)
    n = n//3
print(num)
answer = 0
for i in range(1, len(num)+1):
    if i == 1:
        x = int(num[-i]) * 1
        answer += x
    elif i != 0:
        x = int(num[-i]) * (3**(i-1))
        answer += x

print(answer)
