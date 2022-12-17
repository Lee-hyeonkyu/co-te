al = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
      'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

n = int(input())
s = list(input())

answer = ''

for i in range(0, n, 2):
    x = s[i]
    x_ = int(s[i+1])

    tr = (al.index(x) + (x_**2)) % 26
    answer += al[tr]

print(answer)
