n, m = map(int, input().split())
s = []
k = []
for i in range(m):
    s.append([x for x in map(int, input().split())])
    k.append(s[i][0])
    s[i].pop(0)
p = [y for y in map(int, input().split())]
i = 0
ans = 0
for i in range(2**n):
    on_sum = 0
    for j in range(m):
        for h in range(n):
            if i >> h & 1 and h+1 in s[j]:
                on_sum += 1
        if on_sum%2 != p[j]:
            break
    else:
        ans += 1
print(ans)




