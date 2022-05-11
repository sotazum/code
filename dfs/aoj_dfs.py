# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_11_B&lang=ja
n = int(input())
path = []
path.append([]) #点0はないけど用意
for i in range(n):
    tmp = [int(x) for x in input().split()]
    path.append(tmp[2:])

d = [0]*(n+1)
f = [0]*(n+1)

TIME = 0

def dfs(p, d, f):
    global TIME

    TIME += 1
    d[p] = TIME

    for nxt in path[p]:
        if d[nxt] == 0:
            dfs(nxt, d, f)

    TIME += 1
    f[p] = TIME

    return

for i in range(1, n+1):
    if d[i] == 0:
        dfs(i, d, f)

for i in range(1, n+1):
    print(i, d[i], f[i])
