from collections import deque
n = int(input())
a = [int(x) for x in input().split()]
s = deque([])
for i in range(n):
    if len(s) == 0:
        s.append((1, a[i]))
    elif s[-1][1] != a[i]:
        s.append((1, a[i]))
    elif a[i] == s[-1][1] and a[i] == s[-1][0]+1:
        for j in range(a[i]-1):
            s.pop()
    else:
        s.append((s[-1][0]+1, a[i]))
    print(len(s))





