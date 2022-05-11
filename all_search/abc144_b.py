n = int(input())
count = False
for i in range(1,10):
    for j in range(i,10):
        if i * j == n:
            count = True
if count:
    print('Yes')
else:
    print('No')