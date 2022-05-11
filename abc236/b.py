# import numpy as np
n = int(input())
A = [int(x) for x in input().split()]
x = sum(A)
y = sum(range(1,n+1))*4
print(y-x)

# for i in range(1,n+1):
#     if A.count(i) < 4:
#         print(i)
# counter = np.zeros(n)
# for i in range(len(A)):
#     for j in range(n):
#         if A[i] == j+1:
#             counter[j]+=1
# for j in range(n):
#     if counter[j] != 4:
#         print(j+1)