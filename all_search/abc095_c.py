a, b, c, x, y = map(int, input().split())
u = 0
s = x
t = y
old_yen = a * s + b * t + c * u + 1
for i in range(1, 2*max(x,y)):
    yen = a * s + b * t + c * u
    if yen < old_yen:
        if s>0:
            s -= 1
        if t>0:
            t -= 1
        u = 2 * i
        old_yen = yen
    else: break
print(old_yen)
