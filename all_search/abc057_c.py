import math
n = int(input())
rn = int(math.sqrt(n))
for i in range(1, rn+1):
    if n % i == 0:
        m = int(n/i)
        cnt = 1
        while m >= 10:
            m/=10
            cnt+=1
print(cnt)




