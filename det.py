import numpy as np
n = int(input())
a = []
for i in range(0,n):
    a.append(input().split())
a = np.array(a,dtype=float)
val = np.linalg.det(a)
print(round(val,2))