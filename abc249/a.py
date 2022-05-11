a = [int(x) for x in input().split()]
def takahashi(x,a,b,c):
    time = x // (a+c)
    dis = a*b*time
    if x-(a+c)*time > a:
        return dis + a*b
    else:
        return dis + (x-(a+c)*time)*b

def aoki(x,a,b,c):
    time = x // (a+c)
    dis = a*b*time
    if x-(a+c)*time > a:
        return dis + a*b
    else:
        return dis + (x-(a+c)*time)*b

if takahashi(a[-1],a[0], a[1],a[2]) > aoki(a[-1],a[3], a[4],a[5]):
    print('Takahashi')
elif takahashi(a[-1],a[0], a[1],a[2]) < aoki(a[-1],a[3], a[4],a[5]):
    print('Aoki')
else:
    print('Draw')