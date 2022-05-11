s = input()
l = False
c = False
pool = set()
for i in s:
    if i.islower():
        l = True
    if i.isupper():
        c = True
    if i not in pool:
        pool.add(i)
    else:
        print('No')
        exit(0)
if l and c:
    print('Yes')
else:
    print('No')
