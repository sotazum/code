n, x = map(int, input().split())
a = []
b = []
for i in range(n):
    a1, b1 = map(int, input().split())
    a.append(a1)
    b.append(b1)

dp = [[0]*(x+1) for i in range(n+1)]
# print(dp)
dp[0][0] = 1
# print(dp)
for i in range(n):
    check = []
    for j in range(x+1):
        if dp[i][j] == 1:
            check.append(j)
    for k in check:
        if k+a[i] <= x:
            dp[i+1][k+a[i]] = 1
        if k+b[i] <= x:
            dp[i+1][k+b[i]] = 1
# print(dp)
if dp[n][x] == 1:
    print('Yes')
else:
    print('No')