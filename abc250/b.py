n, a, b = map(int, input().split())
w = '.'*b
b = '#'*b
res = ''
for i in range(n):
    for j in range(a):
        for k in range(n):
            if i % 2:
                if k % 2:
                    res += w
                else:
                    res += b
            else:
                if k % 2:
                    res += b
                else:
                    res += w
            if k == n-1:
                 res += '\n'
print(res)