import sys


S = [0] * 20

N = int(sys.stdin.readline())
for i in range(N):
    x = sys.stdin.readline().split()

    if x[0] == "add":
        S[int(x[1]) - 1] = 1
    elif x[0] == "check":
        print(S[int(x[1]) - 1] & 1)
    elif x[0] == "remove":
        S[int(x[1]) - 1] = 0
    elif x[0] == "toggle":
        S[int(x[1]) - 1] ^= 1
    elif x[0] == "all":
        S = [1] * 20
    else:
        S = [0] * 20
