import itertools

n = int(input())
p = [int(x) for x in input().split()]
q = [int(y) for y in input().split()]
p_all = list(itertools.permutations(p))
q_all = list(itertools.permutations(q))
p_all = sorted(p_all)
q_all = sorted(q_all)
p = tuple(p)
q = tuple(q)
print(abs(p_all.index(p)-q_all.index(q)))
