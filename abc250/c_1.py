import collections



n, q = map(int, input().split())
x = []
res = collections.deque(range(1,n+1))
def right_swap(l: collections.deque, m):
    if l.index(m) == len(l)-1:
        a = l.index(m)
        b = a-1
        tmp = l[a]
        l[a] = l[b]
        l[b] = tmp
    else:
        a = l.index(m)
        b = a + 1
        tmp = l[b]
        l[b] = l[a]
        l[a] = tmp

for i in range(q):
    x.append(int(input()))
for i in x:
    right_swap(res, i)
res = list(res)
print(*res)