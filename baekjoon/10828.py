import sys

input = sys.stdin.readline
lst = []
for _ in range(int(input())):
    comm = input().split()
    str1 = comm[0]
    if str1 == "push":
        lst.append(comm[1])
    elif str1 == "pop":
        if len(lst):
            print(lst.pop())
        else:
            print(-1)
    elif str1 == "top":
        if len(lst):
            print(lst[-1])
        else:
            print(-1)
    elif str1 == "size":
        print(len(lst))
    elif not len(lst):
        print(1)
    else:
        print(0)
