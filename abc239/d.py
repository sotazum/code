a, b, c, d = map(int, input().split())
limit = 200
s_list = []
for i in range(2, limit):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        s_list.append(i)

aoki_list=list(range(c,d+1))
tak = 0
for i in range(a, b+1):
    cnt = 0
    s_list2 = []
    for j in s_list:
        s_list2.append(j-i)
    for k in aoki_list:
        if k in s_list2:
            cnt+=1
    if cnt == 0:
        print('Takahashi')
        tak += 1
        break
    if i == b and tak == 0:
        print('Aoki')



