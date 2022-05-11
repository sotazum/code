x = input()
all_list = []
for i in range(6):
    for j in range(i, 6):
        for k in range(j, 6):
            all_list.append(int(x[i]+x[j]+x[k]))
print(min(all_list))
