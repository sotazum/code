S = str(input())
T = list(S)
a,b = map(int, input().split())
tmp = T[a-1]
T[a-1] = T[b-1]
T[b-1] = tmp
print("".join(T))