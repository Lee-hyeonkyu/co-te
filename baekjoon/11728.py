X, Y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = sorted(A+B)
for i in C:
    print(i, end=" ")
