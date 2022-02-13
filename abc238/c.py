n = int(input())
def f(num):
    num_s = str(num)
    l = len(num_s)-1
    return num-(10**l-1)
res = 0
for i in range(n):
    res += f(i+1)%998244353
print(res)


