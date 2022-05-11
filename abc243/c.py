def rl_c(cl):
    global c
    if c != 0:
        return
    rl = []
    ll = []
    for i in range(len(cl)):
        if cl[i][2] == 'R':
            rl.append(cl[i])
        else:
            ll.append(cl[i])
    if rl != [] and ll != []:
        if min(rl, key=lambda x: x[0]) < max(ll, key=lambda y: y[0]):
            print('Yes')
            c += 1
    return


n = int(input())
xl = []
for i in range(n):
    x, y = map(int, input().split())
    xl.append([x, y])
s = input()
for i in range(n):
    xl[i].append(s[i])
xl_2 = sorted(xl, key=lambda x: x[1])
c_list = []
c = 0
for i in range(n):
    if i == 0:
        continue
    elif i == n-1:
        if xl_2[i][1] == xl_2[i-1][1]:
            c_list.append(xl_2[i - 1])
            c_list.append(xl_2[i])
            rl_c(c_list)
        else:
            c_list.append(xl_2[i - 1])
            rl_c(c_list)
    elif xl_2[i][1] != xl_2[i-1][1]:
        c_list.append(xl_2[i-1])
        if len(c_list) >= 2:
            rl_c(c_list)
        c_list = []
    elif xl_2[i][1] == xl_2[i-1][1]:
        c_list.append(xl_2[i-1])
if c == 0:
    print('No')







