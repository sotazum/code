n, k, x = map(int, input().split())
a = [int(x) for x in input().split()]
ans = 0
def mod(y):
    return y % x
a = list(reversed(sorted(a, key = mod)))
for i in range(n):
    m = a[i]//x
    k -= m
    if k <= 0:
        break
    a[i] = a[i] - m*x
if k <= 0:
    for i in range(n):
        if a[i] > 0:
            ans += a[i]
    print(ans)
else:

# print(a)
# print(k)
    for i in range(n):
        a[i] -= x
        k -= 1
        if k == 0:
            break
    # print(a)
    for i in range(n):
        if a[i] > 0:
            ans += a[i]
    print(ans)