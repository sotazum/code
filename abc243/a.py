v, a, b, c = map(int, input().split())
while v >= 0:
    if v - a < 0:
        print('F')
    elif v - a - b < 0:
        print('M')
    elif v - a - b - c  < 0:
        print('T')
    v = v - a - b - c