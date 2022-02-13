import itertools

n, m = map(int, input().split())
l = []
for i in range(m):
    a, b = map(int, input().split())
    l.append([a, b])
all_n = range(1,n+1)
all_l = list(itertools.permutations(all_n))
# print(l)
all_lt = []
for i in range(len(all_l)):
    if all_l[i][0] == 1:
        all_lt.append(all_l[i])
# print(all_lt)
cnt = 0
for i in range(len(all_l)):
    judge = 0
    for j in range(len(all_l[i])-1):
        check = [all_l[i][j], all_l[i][j+1]]
        if j == 0 and check[0] != 1:
            check = [0, 0]
        check_r = [check[1], check[0]]
        if check_r[1] == 1:
            check_r = [0, 0]
        # print('check', check, i,j)
        if (check in l) or (check_r in l):
            judge += 1
    if judge == len(all_l[i])-1:
        # print('add', judge)
        cnt += 1
print(cnt)