import random
import cmath
from math import e
from mpl_toolkits.mplot3d import axes3d

import matplotlib.pyplot as plt
import numpy as np

list1 = []
list2 = []
output = []


def gen(c1, c2, c3, c4):
    n = 0
    while (n < 500):
        w = random.uniform(-1, 1)
        h = random.uniform(-1, 1)
        m1 = 0
        m2 = 0
        covar = [[0 for i in range(2)] for j in range(2)]
        covar[0][0] = c1
        covar[0][1] = c2
        covar[1][0] = c3
        covar[1][1] = c4
        det = np.linalg.det(covar)
        # print(det)
        a = 1 / ((cmath.pi * 2) * cmath.sqrt(det))
        x1 = np.array([w - m1, h - m2])
        x1t = np.transpose(x1)
        inverse = np.linalg.inv(covar)
        firstm = np.dot(x1t, inverse)
        secondm = np.dot(firstm, x1)
        # print(secondm)
        power = ((-0.5) * secondm)
        b = cmath.e ** power
        anst = a * b
        # y.append(anst)
        if (anst.real >= 0):
            output.append(anst)
            # print(anst)
            list1.append(w)
            list2.append(h)
            # print(w,h)
        n = n + 1


gen(1, 0, 0, 1)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(list1, list2, output)
plt.show()

list1 = []
list2 = []
output = []

gen(0.2, 0, 0, 0.2)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(list1, list2, output)
plt.show()

list1 = []
list2 = []
output = []

gen(2, 0, 0, 2)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(list1, list2, output)
plt.show()

list1 = []
list2 = []
output = []
gen(0.2, 0, 0, 2)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(list1, list2, output)
plt.show()

list1 = []
list2 = []
output = []
gen(2, 0, 0, 0.2)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(list1, list2, output)
plt.show()

list1 = []
list2 = []
output = []
gen(1, 0.5, 0.5, 1)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(list1, list2, output)
plt.show()

list1 = []
list2 = []
output = []
gen(0.3, 0.5, 0.5, 2)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(list1, list2, output)
plt.show()

list1 = []
list2 = []
output = []
gen(0.3, -0.5, -0.5, 2)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(list1, list2, output)
plt.show()