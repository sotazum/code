import itertools
import math

n = int(input())
x = []
for i in range(n):
    xt, yt = map(int, input().split())
    x.append((xt, yt))
x_all = list(itertools.permutations(x))
dist = []
dist_sum = []
for i in range(len(x_all)):
    tmp = []
    for j in range(n-1):
        tmp.append(math.dist(x_all[i][j], x_all[i][j+1]))
    dist.append(tmp)
    dist_sum.append(sum(dist[i]))
ans = sum(dist_sum) / len(x_all)
print(ans)
