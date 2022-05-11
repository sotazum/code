import numpy as np
from functools import lru_cache
def oper(x):
    if x % 2 == 0:
        return int(x/2), int(x/2)
    else:
        return int(x/2), int(x/2)+1

@lru_cache
def chan(l,tmp):
    l_nxt = l
    a, b = oper(l[0])
    l_nxt.pop(0)
    l_nxt.append(a)
    l_nxt.append(b)
    if np.prod(l) < np.prod(l_nxt):
        l = l_nxt
        tmp = []
        print(np.prod(l))
        return chan(l,tmp)
    else:
        tmp.append(l[0])
        l.pop(0)
        l.append(tmp[-1])
        if len(tmp) == len(l):
            return np.prod(l)
        return chan(l,tmp)




x = int(input())
x_list = []
x_list.append(x)
t = []
score = chan(x_list,t)

    # print('score', score)
    # print('old_score', old_score)
print(score%998244353)












