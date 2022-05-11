n, m, k = map(int, input().split())
dp = [[0]*(k+1) for i in range(n+1)]
dp[1][1] = 1
for i in range(1, k+1):
    if i <= m:
        dp[1][i] = 1
    if i <= n:
        dp[i][i] = 1
for i in range(2, n+1):
    for j in range(i+1, k+1):
        for t in range(1, j):
            if j-t+m >= j:
                # print('j', j,'t',t, 'j-t', j-t, 'm', m)
                dp[i][j] += dp[i-1][j-t]
                # print(dp)
# print(dp)
print(sum(dp[n]) % 998244353)






