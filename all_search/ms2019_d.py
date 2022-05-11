n = int(input())
s = list(input())
cnt = 0
for i in range(1000):
    p1 = 300000
    p2 = 300000
    p3 = 300000
    key = []
    key.append(str(int(i/100)))
    i-=100*int(i/100)
    key.append(str(int(i/10)))
    key.append(str(int(i%10)))
    if key[0] in s:
        p1 = s.index(key[0])
        if key[1] in s[p1+1:]:
            p2 = s[p1+1:].index(key[1])+p1+1
            if key[2] in s[p2+1:]:
                p3 = s[p2+1:].index(key[2])+p2+1
    if p1<300000 and p2<300000 and p3<300000:
        cnt += 1
print(cnt)








