a = input()
b = input()
c1 = a[0],a[1]
c1 = "".join(c1)
c1 = int(c1)
c2 = a[3],a[4]
c2 = "".join(c2)
c2 = int(c2)

d1 = b[0],b[1]
d1 = "".join(d1)
d1 = int(d1)
d2 = b[3],b[4]
d2 = "".join(d2)
d2 = int(d2)

t1 = c1 * 60 + c2
t2 = d1 * 60 + d2

t3 = (t1+t2)/2

f1 = int(t3/60)
# print(f1)
t4 = int(t3-(f1*60))
# print(t1)
# print(t2)
f1 = str(f1)
t4 = str(t4)
if(len(f1)==1 and len(t4)==1):
    print("0",end="",)
    print(f1,end="")
    print(":",end="")
    print("0", end="", )
    print(t4)
elif(len(f1)==1):
    print("0",end="",)
    print(f1,end="")
    print(":",end="")
    print(t4)
elif(len(t4)==1):

    print(f1,end="")
    print(":",end="")
    print("0", end="", )
    print(t4)
else:
    print(f1, end="")
    print(":", end="")
    print(t4)