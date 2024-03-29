n = int(input())

d =  [0] * 100_001
d[1] = 1
d[2] = 1
d[3] = 2
d[4] = 3


def dp(n):
	for i in range(5,n+1):
		if not d[i]:
			d[i] = (d[i-2] + d[i-3] + d[i-4]) % 1_000_000_007
	return d[n]
print(dp(n))
'''
d[5] = 4
1 1 1 1 1
3 1 1
1 3 1
1 1 3


d[6] = 6
1 1 1 1 1 1
3 1 1 1
1 3 1 1
1 1 3 1
1 1 1 3
3 3

d[7] = 9
1 1 1 1 1 1 1 
3 1 1 1 1
1 3 1 1 1
1 1 3 1 1
1 1 1 3 1
1 1 1 1 3
3 3 1
3 1 3
1 3 3


1 2 3 4 5 6 7 8
0 0 1 2 3 5 8 12

1 1 2 3 4 6 9 13

d[8]
1 1 1 1 1 1 1 1 
3 1 1 1 1 1
1 3 1 1 1 1
1 1 3 1 1 1
1 1 1 3 1 1
1 1 1 1 3 1
1 1 1 1 1 3
3 3 1 1
3 1 3 1
3 1 1 3
1 3 3 1
1 3 1 3
1 1 3 3
'''