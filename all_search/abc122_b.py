s = list(input())
count_list = []
count = 0
for i in range(len(s)):
    if s[i] == 'A' or s[i] == 'C' or s[i] == 'G' or s[i] == 'T':
        count += 1
    else:
        count_list.append(count)
        count = 0
count_list.append(count)
print(max(count_list))
