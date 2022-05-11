n = int(input())
a = [int(x) for x in input().split()]
b = [int(y) for y in input().split()]
ans_1 = 0
ans_2 = 0
for i in range(n):
    for j in range(n):
        if a[i] == b[j]:
            if i == j:
                ans_1 += 1
            else:
                ans_2 += 1
print(ans_1)
print(ans_2)