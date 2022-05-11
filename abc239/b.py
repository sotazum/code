x = int(input())
x1 = str(x)
if (x >= 0) and (x <= 9):
    print(0)
elif (x >= -9) and (x <= -1):
    print(-1)
elif x >= 0:
    print(int(x1[:-1]))
elif x1[-1] == '0':
    print(int(x1[:-1]))
else:
    print(int(x1[:-1])-1)
