n, x = map(int, input().split())
a = []
b = []
for i in range(n):
    a1, b1 = map(int, input().split())
    a.append(a1)
    b.append(b1)

for i in range(2 ** n):
    ptn = []
    for j in range(n):
        if (i >> j) & 1:
            ptn.append(a[j])
        else:
            ptn.append(b[j])
    s = sum(ptn)
    if s == x:
        print('Yes')
        break
    if i == 2**n -1 and s != x:
        print('No')


