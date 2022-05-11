n, q = map(int, input().split())
x = [int(l) for l in input().split()]
a = []
b = []
for i in range(n-1):
    a1, b1 = map(int, input().split())
    a.append(a1)
    b.append(b1)
v = []
k = []
for i in range(q):
    v1, k1 = map(int, input().split())
    v.append(v1)
    k.append(k1)

