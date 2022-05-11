a, b, k = map(int, input().split())
num = a
cnt = 0
while num < b:
    num *= k
    cnt += 1
print(cnt)