import numpy as np
import cv2

n, m, p = input().split()
n = int(n)
m = int(m)
p = int(p)
a1 = []
a2 = []
for i in range(0, n):
    a1.append(input())
print(a1)
a1 = np.array(a1)
for i in range(0, m):
    a2.append(input())
a2 = np.array(a2)
a3 = np.concatenate((a1, a2), axis=0)
print(a3)