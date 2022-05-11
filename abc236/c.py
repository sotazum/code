n, m = map(int, input().split())
s = [str(x) for x in input().split()]
t = {str(y) for y in input().split()}
for i in range(n):
    if s[i] in t:
        print('Yes')
    else:
        print('No')

