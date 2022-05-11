def count_ones_by_bin(num):
    bin_num = bin(num)[2:]
    count = 0
    for i in bin_num:
            count += int(i)
    return count

n = int(input())
a = []
x = []
y = []
for i in range(n):
    a.append(int(input()))
    x.append([0 for p in range(a[i])])
    y.append([0 for q in range(a[i])])
    for j in range(a[i]):
        u, v = map(int, input().split())
        x[i][j] = u
        y[i][j] = v
old_ans = 0
for i in range(2**n):
    max_num = 0
    ans = 0
    for j in range(n):
        cnt = 0
        if not i >> j & 1:
            for k in range(a[j]):
                if (i >> x[j][k]-1)%2 == y[j][k]:
                    cnt += 1
            if cnt == a[j]:
                break
        else:
            for k in range(a[j]):
                if (i >> x[j][k]-1)%2 == y[j][k]:
                    cnt += 1
            if cnt == a[j]:
                ans += 1
        if ans == count_ones_by_bin(i) and old_ans < ans:
            old_ans = ans
print(old_ans)