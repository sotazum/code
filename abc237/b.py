h, w = map(int, input().split())
a = []
for i in range(h):
    a.append([x for x in input().split()])
b = []
# print(a)
for i in range(w):
    b.append([])
    for j in range(h):
        b[i].append(a[j][i])
for i in range(w):
    print(*b[i])