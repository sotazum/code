h, w = map(int, input().split())
r, c = map(int, input().split())
cnt = 0
if r == 1 or r == h:
    cnt += 1
if c == 1 or c == w:
    cnt += 1
if h == 1:
    cnt += 1
if w == 1:
    cnt += 1
if cnt == 0:
    print(4)
elif cnt == 1:
    print(3)
elif cnt == 2:
    print(2)
elif cnt == 3:
    print(1)
else:
    print(0)

