n = int(input())
a = [int(x) for x in input().split()]
cut_p = 0
cut_p_list = [0, 360]
for i in range(n):
    cut_p += a[i]
    cut_p_list.append(cut_p%360)
cut_p_list.sort()
max_sub = 0
for j in range(len(cut_p_list)-1):
    if cut_p_list[j+1] - cut_p_list[j] > max_sub:
        max_sub = cut_p_list[j+1] - cut_p_list[j]
print(max_sub)

