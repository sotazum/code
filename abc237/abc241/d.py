import copy

query = int(input())
q = []
a = []
at = []
for i in range(query):
    q.append([int(x) for x in input().split()])
    # print(a)
    if len(q[i]) == 2:
        a.append(int(q[i][-1]))
    elif q[i][0] == 2:
        at = copy.copy(a)
        at.append(q[i][1])
        a_s = sorted(at)
        l = a_s.index(q[i][1])
        # print('l', l)
        if len(a_s[:l]) < q[i][2]:
            print(-1)
        else:
            # print('a_s', a_s)
            a_r = list(reversed(a_s[:l]))
            # print('a_r', a_r)
            print(a_r[q[i][2]-1])
    else:
        at = copy.copy(a)
        at.append(q[i][1])
        a_r = sorted(at)
        l = a_r.index(q[i][1])
        # print('l', l)
        if len(a_r[l+1:]) < q[i][2]:
            print(-1)
        else:
            # print('a_r', a_r)
            a_s = a_r[l+1:]
            # print('a_s', a_s)
            print(a_s[q[i][2]-1])
