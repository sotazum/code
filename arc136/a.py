import array
n = int(input())
s = array.array('u',input())
# print(s)
cnt = 0
i = 0
while i < len(s):
    if s[i] == 'A':
        s = s[:i] + array.array('u',['B','B']) + s[i+1:]
    i += 1
    # print(s)
i = 0
while i < len(s):
    if s[i] == 'B':
        cnt += 1
    else:
        cnt = 0
    if cnt == 2:
        s.pop(i-1)
        s.pop(i-1)
        s = s[:i-1] + array.array('u',['A']) + s[i-1:]
        cnt = 0
    else:
        i += 1
s = ''.join(s)
print(s)


