import csv
import random
import numpy as np
mat =[]
with open("ionosphere.csv.txt", 'r') as csvfile:
 reader = csv.reader(csvfile)
 for row in reader:
    mat.append(row)
print(mat)
c1=[]
c2=[]
n = len(mat)
d = len(mat[1])
print(n)
print(d)
print(mat[1][34])
for i in range(0, n):
    if mat[i][d-1] == 'b':
        mat[i].pop()
        c1.append(mat[i])
    else:
        mat[i].pop()
        c2.append(mat[i])
print(d)
d = d-1
print(d)
n1 = len(c1)
n2 = len(c2)
print(n1)
print(len(c1[1]))
sa = []
temp = 0
meana = []
for i in range(0, d):
    sa.append([])
    temp = 0
    for j in range(0, n1):
        sa[i].append(0)
        sa[i][j] = float(c1[j][i])
for i in range(0, d):
    temp = 0
    for j in range(0, n1):
        temp = temp + sa[i][j]
    temp = temp/n
    meana.append(temp)

seco = []
for i in range(0, d):
    seco.append([])
    for j in range(0, n1):
        seco[i].append(0)
        seco[i][j] = sa[i][j]-meana[i]



ansa=[]

for i in range(0,d):
    ansa.append([])
    for j in range (0,d):
        tema=np.array(seco[i])
        temb=np.array(seco[j])
        temb=np.transpose(temb)
        ans1=np.dot(tema,temb)
        ans1 = ans1/(n-1)
        ansa[i].append(0)
        ansa[i][j]=ans1
print(ansa)

sa = []
temp = 0
meana1 = []
for i in range(0, d):
    sa.append([])
    temp = 0
    for j in range(0, n2):
        sa[i].append(0)
        sa[i][j] = float(c2[j][i])
for i in range(0, d):
    temp = 0
    for j in range(0, n2):
        temp = temp + sa[i][j]
    temp = temp/n
    meana1.append(temp)

seco = []
for i in range(0, d):
    seco.append([])
    for j in range(0, n2):
        seco[i].append(0)
        seco[i][j] = sa[i][j]-meana[i]



ansa1=[]

for i in range(0,d):
    ansa1.append([])
    for j in range (0,d):
        tema=np.array(seco[i])
        temb=np.array(seco[j])
        temb=np.transpose(temb)
        ans1=np.dot(tema,temb)
        ans1 = ans1/(n-1)
        ansa1[i].append(0)
        ansa1[i][j]=ans1
print(ansa1)
sw = np.add(ansa, ansa1)
print(np.linalg.det(sw))
swi = np.linalg.inv(sw)
