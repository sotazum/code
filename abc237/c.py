s = input()
def judge_kaibun(s):
    # print(s[:len(s)//2])
    # print(s[len(s) // 2:])
    sr1 = s[len(s) // 2:]
    sr2 = s[(len(s)//2)+1:]
    if len(s) % 2 == 0:
        if s[:len(s)//2] == sr1[::-1]:
            return True
    else:
        if s[:len(s)//2] == sr2[::-1]:
            return True
    return False
sl = len(s)
for i in range(sl):
    if judge_kaibun(s):
        print('Yes')
        break
    elif i == sl-1:
        print('No')
    s = 'a' + s

