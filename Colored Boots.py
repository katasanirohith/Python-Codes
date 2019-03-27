n = int(input())
a = input()
a = list(a)
print(a)
b = input()
b = list(b)
print(b)
for i in range(0,len(a)):
    for j in range (0,len(b)):
        if a[i] == b[j]:
            print(i+1,j+1)
            a.repla
