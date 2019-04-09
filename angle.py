import cmath
ab = int(input())
bc = int(input())
ans1 = float(ab/bc)

ans = cmath.atan(ans1)
final = (cmath.pi/2) - ans
bla = final*(180/cmath.pi)
print(int(round(bla.real,0)),end="")
print("°")