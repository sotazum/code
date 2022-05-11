from functools import lru_cache
n = int(input())
@lru_cache(maxsize=None)

def make_s(k):
    if k == 1:
        return [1]
    else:
        res = []
        for i in range(len(make_s(k-1))):
            res.append(make_s(k-1)[i])
        res.append(k)
        for i in range(len(make_s(k - 1))):
            res.append(make_s(k - 1)[i])
        return res

print(*make_s(n))
