n = int(input())
h = list(map(int, input().split()))
h.append(0)
h.append(0)
dp = [0]*(n+2)
dp[0] = 0
dp[1] = abs(h[1]-h[0])

# print(dp)
# print(h)
for i in range(n-2):
    if dp[i+2] == 0:
        dp[i+2] = min((dp[i+1] + abs(h[i+2] - h[i+1])), (dp[i] + abs(h[i+2] - h[i])))

    # print((dp[i+1] + abs(h[i+2] - h[i+1])), (dp[i] + abs(h[i+2] - h[i])))
    # print('dp', i, '=', dp[i+2])
print(dp[n-1])