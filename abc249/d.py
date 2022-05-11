from operator import mul
import itertools
n = int(input())
a = [int(x) for x in input().split()]
a_list = []
for i in range(n):
    a_shifted = a[i:] + a[:i]
    a_combined = list(map(mul, a, a_shifted))
    a_list.append(a_combined)
cnt = 0
all = list(itertools.chain.from_iterable(a_list))
for i in range(n):
    cnt += all.count(a[i])
print(cnt)
