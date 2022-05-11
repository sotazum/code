n = int(input())
s = input()
x = 'ABC'
count = 0
for i in range(n-2):
    if s[i:i+3] == x:
        count += 1
print(count)