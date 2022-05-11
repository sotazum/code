n = int(input())
s = []
t = []
for i in range(n):
    s1, t1 = map(str, input().split())
    s.append(s1)
    t.append(t1)
cnt = 0
for i in range(n):
    s2 = s[0]
    t2 = t[0]
    s.pop(0)
    t.pop(0)
    # print(s)
    # print(t)
    # print(s2)
    # print(t2)
    if s2 in s and t2 in t:
        print('No')
        break
    if s2 in t and t2 in s:
        print('No')
        break
    if s2 in s and t2 in s:
        print('No')
        break
    if s2 in t and t2 in t:
        print('No')
        break
    s.append(s2)
    t.append(t2)
    cnt += 1
if cnt == n:
    print('Yes')

