n, m = map(int, input().split())
a = [int(x) for x in input().split()]
b = [int(y) for y in input().split()]
for i in range(m):
    if b[i] in a:
        a.remove(b[i])
    else:
        print('No')
        break
if len(a) == n-m:
    print('Yes')

