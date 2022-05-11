n = int(input())
s = []
for i in range(n):
    s.append(input())
    s[i] = list(s[i])
# print(s)



s_i = [[0]*n for i in range(n)]

for i in range(n):
    for j in range(n):
        s_i[i][j] = s[j][i]
# print(s_i)
choice = ['..####', '.#.###', '.##.##', '.###.#', '.####.', '#..###', '#.#.##', '#.##.#', '#.###.', '##..##', '##.#.#', '##.##.', '###..#', '###.#.', '####..', '.#####', '#.####', '##.###', '###.##', '####.#', '#####.', '######']
choice2 = ['#.....', '.#....', '..#...', '...#..', '....#.', '.....#']
choice3 = list(reversed(choice2))
cnt = 0
if choice2 or choice3 in s:
    print('Yes')
    cnt+=1

for i in range(n):
    for j in range(len(choice)):
        if choice[j] in s[i]:
            print('Yes')
            cnt+=1
            break
        if choice[j] in s_i[i]:
            print('Yes')
            cnt+=1
            break
if cnt == 0:
    print('No')



