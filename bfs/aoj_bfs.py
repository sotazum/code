# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_11_C&lang=ja
from collections import deque
n = int(input())
ukv = [list(map(int, input().split())) for _ in range(n)]

distance = [-1]*(n+1)

q = deque()
q.append(1)

distance[1] = 0
while len(q) > 0:
    now = q.popleft()

    for i in range(ukv[now-1][1]):
        node = ukv[now-1][2+i]
        if distance[node] == -1:
            q.append(node)
            distance[node] = distance[now] + 1

for i in range(1, n+1):
    print(i, distance[i])

