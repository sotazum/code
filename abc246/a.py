x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
arrx = [x1, x2, x3]
arry = [y1, y2, y3]
ansx = 0
ansy = 0
for i in range(3):
  if arrx.count(arrx[i]) == 1:
    ansx = arrx[i]
  if arry.count(arry[i]) == 1:
    ansy = arry[i]
print(ansx, ansy)