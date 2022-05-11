n, k = map(int, input().split())
s = []
for i in range(n):
    s.append(input())
note = [[0]*26 for i in range(n)]
for i in range(n):
    for j in s[i]:
        note[i][ord(j)-97] = 1
cnt_list = []
for i in range(2**n):
    cnt = 0
    sub_note = []
    for h in range(n):
        if i >> h & 1:
            sub_note.append(note[h])
    for j in range(26):
        r = [row[j] for row in sub_note]
        if sum(r) == k:
            cnt += 1
    cnt_list.append(cnt)
print(max(cnt_list))
