import cmath
s = input()
real = []
comple =[]
j=0
temp=0
for i in range(0, len(s)):
    if temp == 0:
        if s[i].isdigit():
            real.append(s[i])
        else:
            temp = 1
    if temp ==1:
        if s[i].isdigit():
            comple.append(s[i])
real = "".join(real)
comple = "". join(comple)
real = str(real)
comple =str(comple)
print(real)
print(comple)
ans1 = cmath.phase(complex(int(real), int(comple)))
ans2 = abs(complex(int(real), int(comple)))

print("%.3f" %ans2)
print("%.3f" %ans1)


