import cmath
n = 100
def fucn(i):
    flag=0
    x = cmath.sqrt(i)
    for j in range(2,int(x.real)):
        if i%j == 0:
            flag=1
    if flag == 0:
        print(i,end=" ")
for i in range(1,n):
    fucn(i)