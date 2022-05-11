from collections import deque

q = int(input())
d = deque()
s = 0
for i in range(q):
    tmp = [int(y) for y in input().split()]
    if tmp[0] == 1:
        x = tmp[1]
        c = tmp[2]
        d.append((x, c))
    if tmp[0] == 2:
        cnt = 0
        ans = 0
        c = tmp[1]
        while cnt < c:
            a, b = d.popleft()
            z = min(b, c-cnt)
            ans += a*z
            if b > z:
                d.appendleft((a, b-z))
            cnt += z
        print(ans)





