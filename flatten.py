import numpy as np
n , m = input().split()
n = int(n)
m = int(m)
a = []
for i in range(0,n):
    a.append(list(map(int,input().split())))
a = np.array(a)
t = a.transpose()
f = a.flatten()
print(t)
print(f)