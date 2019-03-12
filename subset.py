n = int(input())
def fucn():
    x = input()
    a = list(map(int,input().split()))
    a = set(a)
    y = input()
    b = list(map(int,input().split()))
    b = set(b)
    if b.issubset(a):
        print("True")
    else:
        print("False")

for i in range(0,n):
    fucn()