n = int(input())
count = 0
for i in range(1, n+1):
    if i < 10:
        count += 1
    elif i >= 10 and i < 100:
        count = count
    elif i >= 100 and i < 1000:
        count += 1
    elif i >= 1000 and i < 10000:
        count = count
    elif i >= 10000 and i < 100000:
        count += 1
print(count)