a, b, k = map(int, input().split())
c = min(a, b)
cnt = 0
for i in range(c+1):
    if a%(c+1-i) == 0 and b%(c+1-i) == 0:
        cnt += 1
        if cnt == k:
            print(c+1-i)

