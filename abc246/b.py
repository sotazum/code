import math
a, b = map(int, input().split())
r = math.sqrt(a*a+b*b)
if a >= 0 and b >= 0:
    print(a/r, b/r)
elif a <= 0 and b >= 0:
    print(-a/r, b/r)
elif a >= 0 and b <= 0:
    print(a/r, -b/r)
elif a <= 0 and b <= 0:
    print(-a/r, -b/r)