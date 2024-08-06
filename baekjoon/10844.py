"""
12
23
34
45
56
67
78
89

98
87
76
65
54
43
32
21
10


123 121
234 232
345 343
456 454
567 565
678 676
789 787
    898
    
987 989
876 878
765 767
654 656
543 545
432 434 
321 323
210 212
101


9  
17  8
32  15  7
61  29  14   7
116 55  26   12 
222 106 51   25 
424

"""

n = int(input())

dp = [[0] * 10 for _ in range(n + 1)]

# for i in range(1, 10):
# dp[0][i] = 1
dp[0] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(1, n + 1):
    dp[i][0] = dp[i - 1][1]
    dp[i][9] = dp[i - 1][8]

    for j in range(1, 9):
        dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

print(sum(dp[n - 1]) % 1_000_000_000)
