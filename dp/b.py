n, k = map(int, input().split())
h_tmp = list(map(int, input().split()))
h = [0]
for i in h_tmp:
    h.append(i)
dp = [0]*(n+1)
dp[0] = 0
dp[1] = 0
dp[2] = abs(h[2]-h[1])
# print('h=', h)
for i in range(1, n+1):
    cost = []
    if dp[i] <= 0:
        for j in range(1, k+1):
            if i-j > 0:
                cost.append(dp[i-j] + abs(h[i]-h[i-j]))
    if cost != []:
        dp[i] = min(cost)
    # print('cost', i,  cost)
    #
    # print('dp', i, dp)
print(dp[n])
