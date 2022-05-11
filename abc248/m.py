a = 315
b = 840
while b >0:
    a %= b
    tmp = a
    a = b
    b =tmp
print(a)