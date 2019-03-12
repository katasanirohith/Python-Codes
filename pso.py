import random
import cmath
def eval(x):
    return cmath.sin(x)
pos = []
vel = []
eva = []
pbest =[]
n=int(input("Enter population size"))
for i in range(0, n):
    x = random.random()
    x = x * 2
    x = x * cmath.pi
    pos.append(x)
    pbest.append(x)

for i in range(0, n):
    eva.append(eval(pos[i]).real)

posm = 0
velm = 0
num = 10
while num>0:
    evam = min(eva)
    eval1=[]
    for i in range(0,n):
        if evam == eva[i]:
            posm = pos[i]
            velm = vel[i]
            gbest = evam
    for i in range(0, n):
        x = random.random()
        x = x * 2
        x = x * cmath.pi
        vel.append(x)
    for i in range(0, n):
        pos[i] += vel[i]
        eval1.append(eval(pos[i]))
        if eva[i] > eval1[i]:
            pbest[i] = pos[i]
        eva[i] = eval1[i]
    temp = min(eval(pbest))
    for i in range(0,n):
        if temp == eval(pbest[i]):
            gbest = pos[i]
    num -= 1



