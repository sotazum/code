n = int(input())
array = []
happy = 0
for i in range(n):
    x = list(map(int, input().split()))
    array.append(x)
dp = [[0 for i in range(n)] for j in range(3)]
for i in range(n):
    for j in range(3):
        for k in range(3):
        if i == 0:
            dp[j][i] = array[i][j]
            if j == k:
                continue
            dp1 = dp[j][i-1] + array[i][k]
            if dp1 > dp[j][i-1]:






