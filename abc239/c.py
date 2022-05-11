import math
r5 = math.sqrt(5)
x1, y1, x2, y2 = map(int, input().split())
def dst(x1,y1,x2,y2):
    return x1*x1 + x2*x2 - 2*x1*x2 + y1*y1 + y2*y2 - 2*y1*y2
max_x1 = int(x1+r5)
min_x1 = int(x1-r5)

max_y1 = int(y1+r5)
min_y1 = int(y1-r5)

max_x2 = int(x2+r5)
min_x2 = int(x2-r5)

max_y2 = int(y2+r5)
min_y2 = int(y2-r5)

list_1 = []
for i in range(min_x1, max_x1+1):
    for j in range(min_y1, max_y1+1):
        list_1.append((i,j))
list_2 = []
for i in range(min_x2, max_x2+1):
    for j in range(min_y2, max_y2+1):
        list_2.append((i,j))

# print(list_1)
# print(list_2)


pool = set(list_1) & set(list_2)
pool = list(pool)
# print(pool)
cnt = 0
for i in range(len(pool)):
    dst1 = dst(pool[i][0], pool[i][1], x1, y1)
    dst2 = dst(pool[i][0], pool[i][1], x2, y2)
    # print(dst1, dst2)
    if dst1 == 5 and dst2 == 5:
        cnt += 1
if cnt == 0:
    print('No')
else:
    print('Yes')




